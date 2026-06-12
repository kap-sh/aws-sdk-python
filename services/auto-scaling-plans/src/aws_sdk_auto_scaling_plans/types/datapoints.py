"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#Datapoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.datapoint

Datapoints: TypeAlias = list["aws_sdk_auto_scaling_plans.types.datapoint.Datapoint"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Datapoints) -> list:
    import aws_sdk_auto_scaling_plans.types.datapoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auto_scaling_plans.types.datapoint.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Datapoints:
    import aws_sdk_auto_scaling_plans.types.datapoint

    out: Datapoints = []
    for item in data:
        out.append(
            aws_sdk_auto_scaling_plans.types.datapoint.deserialize_aws_json_1_1(item)
        )
    return out
