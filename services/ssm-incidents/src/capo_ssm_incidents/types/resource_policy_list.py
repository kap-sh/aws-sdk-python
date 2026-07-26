"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ResourcePolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.resource_policy

ResourcePolicyList: TypeAlias = list[
    "capo_ssm_incidents.types.resource_policy.ResourcePolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePolicyList) -> list:
    import capo_ssm_incidents.types.resource_policy

    out: list = []
    for item in value:
        out.append(capo_ssm_incidents.types.resource_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourcePolicyList:
    import capo_ssm_incidents.types.resource_policy

    out: ResourcePolicyList = []
    for item in data:
        out.append(capo_ssm_incidents.types.resource_policy.deserialize_json(item))
    return out
