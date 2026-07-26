"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_status
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.timestamp


class BotVersionSummary(TypedDict, closed=True):
    bot_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name of the bot associated with the version.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The numeric version of the bot, or <code>DRAFT</code> to indicate that this is the version of the bot that can be updated..</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description of the version.</p>"""
    bot_status: NotRequired["capo_lex_models_v2.types.bot_status.BotStatus"]
    """<p>The status of the bot. When the status is available, the version of the bot is ready for use.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the version was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotVersionSummary) -> dict:
    out: dict = {}
    if "bot_name" in value:
        out["botName"] = value["bot_name"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "bot_status" in value:
        import capo_lex_models_v2.types.bot_status

        out["botStatus"] = capo_lex_models_v2.types.bot_status.serialize_json(
            value["bot_status"]
        )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    return out


def deserialize_json(data: dict) -> BotVersionSummary:
    out: BotVersionSummary = {}  # type: ignore[typeddict-item]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "description" in data:
        out["description"] = data["description"]
    if "botStatus" in data:
        import capo_lex_models_v2.types.bot_status

        out["bot_status"] = capo_lex_models_v2.types.bot_status.deserialize_json(
            data["botStatus"]
        )
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    return out
