"""Generated from Smithy shape ``com.amazonaws.connect#GroupingsV2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.grouping_v2

GroupingsV2: TypeAlias = list["aws_sdk_connect.types.grouping_v2.GroupingV2"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingsV2) -> list:
    return list(value)


def deserialize_json(data: list) -> GroupingsV2:
    return list(data)
