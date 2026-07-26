"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#MappingRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rolesanywhere.types.mapping_rule

MappingRules: TypeAlias = list["capo_rolesanywhere.types.mapping_rule.MappingRule"]


# --- restJson1 ser/de ---
def serialize_json(value: MappingRules) -> list:
    import capo_rolesanywhere.types.mapping_rule

    out: list = []
    for item in value:
        out.append(capo_rolesanywhere.types.mapping_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> MappingRules:
    import capo_rolesanywhere.types.mapping_rule

    out: MappingRules = []
    for item in data:
        out.append(capo_rolesanywhere.types.mapping_rule.deserialize_json(item))
    return out
