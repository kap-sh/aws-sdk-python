"""Generated from Smithy shape ``com.amazonaws.costexplorer#DeleteAnomalySubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class DeleteAnomalySubscriptionRequest(TypedDict):
    subscription_arn: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>The unique identifier of the cost anomaly subscription that you want to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAnomalySubscriptionRequest) -> dict:
    out: dict = {}
    out["SubscriptionArn"] = value["subscription_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAnomalySubscriptionRequest:
    out: DeleteAnomalySubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "SubscriptionArn" in data:
        out["subscription_arn"] = data["SubscriptionArn"]
    else:
        raise DeserializationError(
            "DeleteAnomalySubscriptionRequest.subscription_arn required"
        )
    return out
