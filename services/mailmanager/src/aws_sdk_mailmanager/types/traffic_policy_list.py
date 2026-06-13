"""Generated from Smithy shape ``com.amazonaws.mailmanager#TrafficPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.traffic_policy

TrafficPolicyList: TypeAlias = list[
    "aws_sdk_mailmanager.types.traffic_policy.TrafficPolicy"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TrafficPolicyList) -> list:
    import aws_sdk_mailmanager.types.traffic_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mailmanager.types.traffic_policy.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TrafficPolicyList:
    import aws_sdk_mailmanager.types.traffic_policy

    out: TrafficPolicyList = []
    for item in data:
        out.append(
            aws_sdk_mailmanager.types.traffic_policy.deserialize_aws_json_1_0(item)
        )
    return out
