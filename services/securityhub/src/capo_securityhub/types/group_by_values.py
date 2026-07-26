"""Generated from Smithy shape ``com.amazonaws.securityhub#GroupByValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.group_by_value

GroupByValues: TypeAlias = list["capo_securityhub.types.group_by_value.GroupByValue"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupByValues) -> list:
    import capo_securityhub.types.group_by_value

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.group_by_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupByValues:
    import capo_securityhub.types.group_by_value

    out: GroupByValues = []
    for item in data:
        out.append(capo_securityhub.types.group_by_value.deserialize_json(item))
    return out
