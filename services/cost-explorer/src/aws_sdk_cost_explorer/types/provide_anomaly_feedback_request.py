"""Generated from Smithy shape ``com.amazonaws.costexplorer#ProvideAnomalyFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.anomaly_feedback_type
    import aws_sdk_cost_explorer.types.generic_string


class ProvideAnomalyFeedbackRequest(TypedDict, closed=True):
    anomaly_id: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>A cost anomaly ID. </p>"""
    feedback: "aws_sdk_cost_explorer.types.anomaly_feedback_type.AnomalyFeedbackType"
    """<p>Describes whether the cost anomaly was a planned activity or you considered it an anomaly. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvideAnomalyFeedbackRequest) -> dict:
    out: dict = {}
    out["AnomalyId"] = value["anomaly_id"]
    import aws_sdk_cost_explorer.types.anomaly_feedback_type

    out["Feedback"] = (
        aws_sdk_cost_explorer.types.anomaly_feedback_type.serialize_aws_json_1_1(
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
        import aws_sdk_cost_explorer.types.anomaly_feedback_type

        out["feedback"] = (
            aws_sdk_cost_explorer.types.anomaly_feedback_type.deserialize_aws_json_1_1(
                data["Feedback"]
            )
        )
    else:
        raise DeserializationError("ProvideAnomalyFeedbackRequest.feedback required")
    return out
