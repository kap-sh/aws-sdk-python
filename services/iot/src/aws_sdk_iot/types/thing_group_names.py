"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_group_name

ThingGroupNames: TypeAlias = list["aws_sdk_iot.types.thing_group_name.ThingGroupName"]


# --- restJson1 ser/de ---
def serialize_json(value: ThingGroupNames) -> list:
    return list(value)


def deserialize_json(data: list) -> ThingGroupNames:
    return list(data)
