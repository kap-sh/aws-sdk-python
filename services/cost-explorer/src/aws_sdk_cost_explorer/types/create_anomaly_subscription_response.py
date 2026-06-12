"""Generated from Smithy shape ``com.amazonaws.costexplorer#CreateAnomalySubscriptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class CreateAnomalySubscriptionResponse(TypedDict):
    subscription_arn: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>The unique identifier of your newly created cost anomaly subscription. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAnomalySubscriptionResponse) -> dict:
    out: dict = {}
    out["SubscriptionArn"] = value["subscription_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAnomalySubscriptionResponse:
    out: CreateAnomalySubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "SubscriptionArn" in data:
        out["subscription_arn"] = data["SubscriptionArn"]
    else:
        raise DeserializationError(
            "CreateAnomalySubscriptionResponse.subscription_arn required"
        )
    return out
