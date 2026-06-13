"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ResourcePolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.resource_policy

ResourcePolicyList: TypeAlias = list[
    "aws_sdk_ssm_incidents.types.resource_policy.ResourcePolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePolicyList) -> list:
    import aws_sdk_ssm_incidents.types.resource_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_incidents.types.resource_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourcePolicyList:
    import aws_sdk_ssm_incidents.types.resource_policy

    out: ResourcePolicyList = []
    for item in data:
        out.append(aws_sdk_ssm_incidents.types.resource_policy.deserialize_json(item))
    return out
