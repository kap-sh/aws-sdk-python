"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAcknowledgementSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.evaluation_acknowledger_comment_string
    import capo_connect.types.timestamp


class EvaluationAcknowledgementSummary(TypedDict, closed=True):
    acknowledged_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The time when an agent acknowledged the evaluation.</p>"""
    acknowledged_by: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The agent who acknowledged the evaluation.</p>"""
    acknowledger_comment: NotRequired[
        "capo_connect.types.evaluation_acknowledger_comment_string.EvaluationAcknowledgerCommentString"
    ]
    """<p>A comment from the agent when they confirmed they acknowledged the evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAcknowledgementSummary) -> dict:
    out: dict = {}
    if "acknowledged_time" in value:
        import capo_connect.types.timestamp

        out["AcknowledgedTime"] = capo_connect.types.timestamp.serialize_json(
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
        import capo_connect.types.timestamp

        out["acknowledged_time"] = capo_connect.types.timestamp.deserialize_json(
            data["AcknowledgedTime"]
        )
    if "AcknowledgedBy" in data:
        out["acknowledged_by"] = data["AcknowledgedBy"]
    if "AcknowledgerComment" in data:
        out["acknowledger_comment"] = data["AcknowledgerComment"]
    return out
