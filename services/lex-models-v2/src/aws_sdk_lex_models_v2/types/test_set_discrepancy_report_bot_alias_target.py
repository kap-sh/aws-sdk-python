"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetDiscrepancyReportBotAliasTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_id
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class TestSetDiscrepancyReportBotAliasTarget(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier for the bot alias.</p>"""
    bot_alias_id: "aws_sdk_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The unique identifier for the bot associated with the bot alias.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The unique identifier of the locale associated with the bot alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetDiscrepancyReportBotAliasTarget) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botAliasId"] = value["bot_alias_id"]
    out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> TestSetDiscrepancyReportBotAliasTarget:
    out: TestSetDiscrepancyReportBotAliasTarget = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    else:
        raise DeserializationError(
            "TestSetDiscrepancyReportBotAliasTarget.bot_id required"
        )
    if "botAliasId" in data:
        out["bot_alias_id"] = data["botAliasId"]
    else:
        raise DeserializationError(
            "TestSetDiscrepancyReportBotAliasTarget.bot_alias_id required"
        )
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    else:
        raise DeserializationError(
            "TestSetDiscrepancyReportBotAliasTarget.locale_id required"
        )
    return out
