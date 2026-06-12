"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalySubscriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.anomaly_subscription

AnomalySubscriptions: TypeAlias = list[
    "aws_sdk_cost_explorer.types.anomaly_subscription.AnomalySubscription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalySubscriptions) -> list:
    import aws_sdk_cost_explorer.types.anomaly_subscription

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.anomaly_subscription.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AnomalySubscriptions:
    import aws_sdk_cost_explorer.types.anomaly_subscription

    out: AnomalySubscriptions = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.anomaly_subscription.deserialize_aws_json_1_1(
                item
            )
        )
    return out
