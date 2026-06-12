"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAcknowledgementSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.evaluation_acknowledger_comment_string
    import aws_sdk_connect.types.timestamp


class EvaluationAcknowledgementSummary(TypedDict):
    acknowledged_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The time when an agent acknowledged the evaluation.</p>"""
    acknowledged_by: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The agent who acknowledged the evaluation.</p>"""
    acknowledger_comment: NotRequired[
        "aws_sdk_connect.types.evaluation_acknowledger_comment_string.EvaluationAcknowledgerCommentString"
    ]
    """<p>A comment from the agent when they confirmed they acknowledged the evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAcknowledgementSummary) -> dict:
    out: dict = {}
    if "acknowledged_time" in value:
        import aws_sdk_connect.types.timestamp

        out["AcknowledgedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["acknowledged_time"]
        )
    if "acknowledged_by" in value:
        out["AcknowledgedBy"] = value["acknowledged_by"]
    if "acknowledger_comment" in value:
        out["AcknowledgerComment"] = value["acknowledger_comment"]
    return out


def deserialize_json(data: dict) -> EvaluationAcknowledgementSummary:
    out: EvaluationAcknowledgementSummary = {}  # type: ignore[typeddict-item]
    if "AcknowledgedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["acknowledged_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["AcknowledgedTime"]
        )
    if "AcknowledgedBy" in data:
        out["acknowledged_by"] = data["AcknowledgedBy"]
    if "AcknowledgerComment" in data:
        out["acknowledger_comment"] = data["AcknowledgerComment"]
    return out
