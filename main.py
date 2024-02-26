import interactions, datetime
from interactions import *
from interactions import OptionType, InteractionType, Client, Intents
from interactions.models import application_commands_to_dict
from interactions import slash_command, slash_option, Embed, EmbedAuthor, EmbedAttachment, EmbedFooter
from interactions import Modal, ShortText, ModalContext, ParagraphText, SlashContext, slash_command, SlashCommandChoice
from interactions import Button, ButtonStyle, ActionRow
import typing
from typing import Union
from interactions.api.events import Component
import asyncio
import discord
from discord.ext import commands
# from dislash import InteractionClient, slash_command, Button, ButtonStyle

bot = Client(intents=Intents.DEFAULT)
client = Client()




# Button
   
# @slash_command(
#     name="buttons",
#     description="Send buttons",
# )
# async def buttons(ctx: SlashContext):
#     button = Button(
#         style=ButtonStyle.PRIMARY,
#         custom_id="primary",
#         label="Blue Button",
#     )
#     await ctx.send("This is a Button", components=[button])
        
        


#== Erstelle ein Spielangebot
@slash_command(
    name="angebot",
    description="Send a table offer",
)
async def buttons(ctx: SlashContext):
    button = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="primary",
        label="Create a Game",
    )
    await ctx.send("Create a Game", components=[button])
@listen(Component)
async def on_comp(event: Component):
    ctx = event.ctx
    
    my_modal = Modal(
        ShortText(
            label="Spiel Name",
            custom_id="game_name",
            placeholder="The Legends of ...",
        ),
        ShortText(
            label="Datum",
            custom_id="play_date",
            required=True,
            placeholder="01.01.1000",
        ),
        ShortText(
            label="Uhrzeit",
            custom_id="play_time",
            required=True,
            placeholder="00:00",
        ),
        ParagraphText(
            label="Beschreibung",
            custom_id="play_des",
            required=True,
            placeholder="Kurze Beschreibung",
            max_length= 200
        ),

        title="Table Offer",
    )
    
    match ctx.custom_id:
        case "primary":
            await ctx.send_modal(modal=my_modal)
            
            # Allow a short delay for the original interaction response to be processed
            await asyncio.sleep(1)
            
            modal_ctx: ModalContext = await ctx.bot.wait_for_modal(my_modal)
            
            
            # extract the answers from the responses dictionary
            game_name = modal_ctx.responses["game_name"]
            play_date = modal_ctx.responses["play_date"]
            play_time = modal_ctx.responses["play_time"]
            play_des = modal_ctx.responses["play_des"]
            
            embed = interactions.Embed(
                title="Angebot",
                description=f'**{game_name}** \n\n {play_date} \n\n {play_time} Uhr \n\n {play_des}',
                thumbnail=interactions.EmbedAttachment(url=ctx.author.avatar.url),
                footer=interactions.EmbedFooter(text=f'Gesendet von {ctx.author.display_name}'),
                timestamp=datetime.datetime.now(),
                color=0x3498db
            )
            # Determine the channel where the message should be sent
            # target_channel_id = 1207112414936694814
            
            # await ctx.channel.send(1207112414936694814, f'Das Angebot wurde gesendet', ephemeral=True)
            # await modal_ctx.send(embed=embed)
            
                        # Determine the channel where the message should be sent 1207112414936694814
            #target_channel_id = 1198934055199182858 #|| Dungeon and Dumbasses Server
            target_channel_id = 1207112414936694814  #|| est Server
            
            # Get the TextChannel object
            target_channel = ctx.bot.get_channel(target_channel_id)
            
            if target_channel:
                await ctx.send(f'Message incoming...', ephemeral=True)
                await target_channel.send(embed=embed)
                # Schedule the modal closing after the initial response
                asyncio.create_task(ctx.send_modal(modal=None))
            else:
                await ctx.send(f'Ungültiger Channel ID', ephemeral=True)



# ======================
# Add Role / Remove Role (currently nor working)
# ======================
@slash_command(
    name="add_role",
    description="Give a role"
)
async def add_role(ctx: SlashContext):
    role = ctx.guild.get_role(1210596582387490877)
    await Member.add_roles(role.id)


# ======================
# Add Role / Remove Role 2 (currently nor working)
# ======================

@slash_command(name="give_role")
async def give_role(ctx: SlashContext, role: Role):
    await ctx.author.add_roles(1210596582387490877)
    await ctx.send(f"Die Rolle {role.name} wurde dir erfolgreich gegeben.")












#== Tool Command (soll ein Button werden, der die Nachricht per DM verschickt.)
# @slash_command(
#     name="info",
#     description="Send 5eTools infos",
#     sub_cmd_name="books",
#     sub_cmd_description="My subcommand",
# )
# async def buttons(ctx: SlashContext):
#     button = Button(
#         style=ButtonStyle.WARNING,
#         custom_id="info-button",
#         label="Info Button",
#     )
#     await ctx.send("Create a Game", components=[button])
# async def my_second_command_function(ctx: SlashContext):
#     embed = interactions.Embed(
#         title="**We play mainly with follow books:**",
#         description=f'**We play mainly with follow books:**',
#         footer=interactions.EmbedFooter(text=f'Gesendet von {ctx.author.display_name}'),
#         color=0x3498db
#     )
#     await ctx.send(f'Message incoming...', ephemeral=True)
#     await ctx.send(embed=embed)









# created by Marlon Lange (MLangeEU) / HolyCodez

bot.start('YOUR_BOT_TOKEN')
