"""Generated from Smithy shape ``com.amazonaws.deadline#UsageGroupBy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.usage_group_by_field

UsageGroupBy: TypeAlias = list[
    "capo_deadline.types.usage_group_by_field.UsageGroupByField"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageGroupBy) -> list:
    import capo_deadline.types.usage_group_by_field

    out: list = []
    for item in value:
        out.append(capo_deadline.types.usage_group_by_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageGroupBy:
    import capo_deadline.types.usage_group_by_field

    out: UsageGroupBy = []
    for item in data:
        out.append(capo_deadline.types.usage_group_by_field.deserialize_json(item))
    return out
