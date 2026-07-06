"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartBotAnalyzerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analysis_scope
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class StartBotAnalyzerRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot to analyze.</p>"""
    analysis_scope: "aws_sdk_lex_models_v2.types.analysis_scope.AnalysisScope"
    """<p>The scope of analysis to perform. Currently only <code>BotLocale</code> scope is supported.</p> <p>Valid Values: <code>BotLocale</code> </p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale identifier for the bot locale to analyze. Required when <code>analysisScope</code> is <code>BotLocale</code>.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot to analyze. Defaults to <code>DRAFT</code> if not specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBotAnalyzerRequest) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analysis_scope

    out["analysisScope"] = aws_sdk_lex_models_v2.types.analysis_scope.serialize_json(
        value["analysis_scope"]
    )
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    return out


def deserialize_json(data: dict) -> StartBotAnalyzerRequest:
    out: StartBotAnalyzerRequest = {}  # type: ignore[typeddict-item]
    if "analysisScope" in data:
        import aws_sdk_lex_models_v2.types.analysis_scope

        out["analysis_scope"] = (
            aws_sdk_lex_models_v2.types.analysis_scope.deserialize_json(
                data["analysisScope"]
            )
        )
    else:
        raise DeserializationError("StartBotAnalyzerRequest.analysis_scope required")
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    return out
