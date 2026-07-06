"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAnalyzerHistorySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_analyzer_status
    import aws_sdk_lex_models_v2.types.timestamp
    import aws_sdk_lex_models_v2.types.uuid


class BotAnalyzerHistorySummary(TypedDict, closed=True):
    bot_analyzer_status: (
        "aws_sdk_lex_models_v2.types.bot_analyzer_status.BotAnalyzerStatus"
    )
    """<p>The status of the historical analysis execution.</p> <p>Valid Values: <code>Processing | Available | Failed | Stopping | Stopped</code> </p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the analysis was initiated.</p>"""
    bot_analyzer_request_id: "aws_sdk_lex_models_v2.types.uuid.UUID"
    """<p>The unique identifier for the analysis request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotAnalyzerHistorySummary) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.bot_analyzer_status

    out["botAnalyzerStatus"] = (
        aws_sdk_lex_models_v2.types.bot_analyzer_status.serialize_json(
            value["bot_analyzer_status"]
        )
    )
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    out["botAnalyzerRequestId"] = value["bot_analyzer_request_id"]
    return out


def deserialize_json(data: dict) -> BotAnalyzerHistorySummary:
    out: BotAnalyzerHistorySummary = {}  # type: ignore[typeddict-item]
    if "botAnalyzerStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_analyzer_status

        out["bot_analyzer_status"] = (
            aws_sdk_lex_models_v2.types.bot_analyzer_status.deserialize_json(
                data["botAnalyzerStatus"]
            )
        )
    else:
        raise DeserializationError(
            "BotAnalyzerHistorySummary.bot_analyzer_status required"
        )
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "botAnalyzerRequestId" in data:
        out["bot_analyzer_request_id"] = data["botAnalyzerRequestId"]
    else:
        raise DeserializationError(
            "BotAnalyzerHistorySummary.bot_analyzer_request_id required"
        )
    return out
