"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceGroupByRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.resource_group_by_rule

ResourceGroupByRules: TypeAlias = list[
    "capo_securityhub.types.resource_group_by_rule.ResourceGroupByRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceGroupByRules) -> list:
    import capo_securityhub.types.resource_group_by_rule

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.resource_group_by_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceGroupByRules:
    import capo_securityhub.types.resource_group_by_rule

    out: ResourceGroupByRules = []
    for item in data:
        out.append(capo_securityhub.types.resource_group_by_rule.deserialize_json(item))
    return out
