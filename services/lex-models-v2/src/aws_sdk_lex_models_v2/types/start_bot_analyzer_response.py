"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartBotAnalyzerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_analyzer_status
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.timestamp
    import aws_sdk_lex_models_v2.types.uuid


class StartBotAnalyzerResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot being analyzed.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot being analyzed.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale identifier of the bot locale being analyzed.</p>"""
    bot_analyzer_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_analyzer_status.BotAnalyzerStatus"
    ]
    """<p>The current status of the analysis. The initial status is <code>Processing</code>.</p> <p>Valid Values: <code>Processing | Available | Failed | Stopping | Stopped</code> </p>"""
    bot_analyzer_request_id: NotRequired["aws_sdk_lex_models_v2.types.uuid.UUID"]
    """<p>A unique identifier for this analysis request. Use this identifier to check the status and retrieve results.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the analysis was initiated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBotAnalyzerResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_analyzer_status" in value:
        import aws_sdk_lex_models_v2.types.bot_analyzer_status

        out["botAnalyzerStatus"] = (
            aws_sdk_lex_models_v2.types.bot_analyzer_status.serialize_json(
                value["bot_analyzer_status"]
            )
        )
    if "bot_analyzer_request_id" in value:
        out["botAnalyzerRequestId"] = value["bot_analyzer_request_id"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    return out


def deserialize_json(data: dict) -> StartBotAnalyzerResponse:
    out: StartBotAnalyzerResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botAnalyzerStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_analyzer_status

        out["bot_analyzer_status"] = (
            aws_sdk_lex_models_v2.types.bot_analyzer_status.deserialize_json(
                data["botAnalyzerStatus"]
            )
        )
    if "botAnalyzerRequestId" in data:
        out["bot_analyzer_request_id"] = data["botAnalyzerRequestId"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    return out
