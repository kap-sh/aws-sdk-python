"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StopBotAnalyzerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_analyzer_status
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.uuid


class StopBotAnalyzerResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale identifier of the bot locale.</p>"""
    bot_analyzer_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_analyzer_status.BotAnalyzerStatus"
    ]
    """<p>The updated status of the analysis. The status will be <code>Stopping</code> and will eventually transition to <code>Stopped</code>.</p> <p>Valid Values: <code>Processing | Available | Failed | Stopping | Stopped</code> </p>"""
    bot_analyzer_request_id: NotRequired["aws_sdk_lex_models_v2.types.uuid.UUID"]
    """<p>The unique identifier of the analysis request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopBotAnalyzerResponse) -> dict:
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
    return out


def deserialize_json(data: dict) -> StopBotAnalyzerResponse:
    out: StopBotAnalyzerResponse = {}  # type: ignore[typeddict-item]
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
    return out
