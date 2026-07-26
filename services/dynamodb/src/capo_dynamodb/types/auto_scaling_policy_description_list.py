"""Generated from Smithy shape ``com.amazonaws.dynamodb#AutoScalingPolicyDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.auto_scaling_policy_description

AutoScalingPolicyDescriptionList: TypeAlias = list[
    "capo_dynamodb.types.auto_scaling_policy_description.AutoScalingPolicyDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingPolicyDescriptionList) -> list:
    import capo_dynamodb.types.auto_scaling_policy_description

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.auto_scaling_policy_description.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutoScalingPolicyDescriptionList:
    import capo_dynamodb.types.auto_scaling_policy_description

    out: AutoScalingPolicyDescriptionList = []
    for item in data:
        out.append(
            capo_dynamodb.types.auto_scaling_policy_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out
