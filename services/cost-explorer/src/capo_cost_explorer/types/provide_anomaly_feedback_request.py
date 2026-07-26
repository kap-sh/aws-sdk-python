"""Generated from Smithy shape ``com.amazonaws.costexplorer#ProvideAnomalyFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.anomaly_feedback_type
    import capo_cost_explorer.types.generic_string


class ProvideAnomalyFeedbackRequest(TypedDict, closed=True):
    anomaly_id: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>A cost anomaly ID. </p>"""
    feedback: "capo_cost_explorer.types.anomaly_feedback_type.AnomalyFeedbackType"
    """<p>Describes whether the cost anomaly was a planned activity or you considered it an anomaly. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvideAnomalyFeedbackRequest) -> dict:
    out: dict = {}
    out["AnomalyId"] = value["anomaly_id"]
    import capo_cost_explorer.types.anomaly_feedback_type

    out["Feedback"] = (
        capo_cost_explorer.types.anomaly_feedback_type.serialize_aws_json_1_1(
            value["feedback"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvideAnomalyFeedbackRequest:
    out: ProvideAnomalyFeedbackRequest = {}  # type: ignore[typeddict-item]
    if "AnomalyId" in data:
        out["anomaly_id"] = data["AnomalyId"]
    else:
        raise DeserializationError("ProvideAnomalyFeedbackRequest.anomaly_id required")
    if "Feedback" in data:
        import capo_cost_explorer.types.anomaly_feedback_type

        out["feedback"] = (
            capo_cost_explorer.types.anomaly_feedback_type.deserialize_aws_json_1_1(
                data["Feedback"]
            )
        )
    else:
        raise DeserializationError("ProvideAnomalyFeedbackRequest.feedback required")
    return out
