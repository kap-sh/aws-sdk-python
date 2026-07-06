"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasHistoryEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.timestamp


class BotAliasHistoryEvent(TypedDict, closed=True):
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot that was used in the event. </p>"""
    start_date: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the event started.</p>"""
    end_date: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the event ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasHistoryEvent) -> dict:
    out: dict = {}
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "start_date" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["startDate"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["start_date"]
        )
    if "end_date" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["endDate"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["end_date"]
        )
    return out


def deserialize_json(data: dict) -> BotAliasHistoryEvent:
    out: BotAliasHistoryEvent = {}  # type: ignore[typeddict-item]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "startDate" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["start_date"] = aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
            data["startDate"]
        )
    if "endDate" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["end_date"] = aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
            data["endDate"]
        )
    return out
