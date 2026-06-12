"""Generated from Smithy shape ``com.amazonaws.costexplorer#ProvideAnomalyFeedbackResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class ProvideAnomalyFeedbackResponse(TypedDict):
    anomaly_id: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>The ID of the modified cost anomaly. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvideAnomalyFeedbackResponse) -> dict:
    out: dict = {}
    out["AnomalyId"] = value["anomaly_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvideAnomalyFeedbackResponse:
    out: ProvideAnomalyFeedbackResponse = {}  # type: ignore[typeddict-item]
    if "AnomalyId" in data:
        out["anomaly_id"] = data["AnomalyId"]
    else:
        raise DeserializationError("ProvideAnomalyFeedbackResponse.anomaly_id required")
    return out
