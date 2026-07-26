"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupNameAndArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.group_name_and_arn

ThingGroupNameAndArnList: TypeAlias = list[
    "capo_iot.types.group_name_and_arn.GroupNameAndArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThingGroupNameAndArnList) -> list:
    import capo_iot.types.group_name_and_arn

    out: list = []
    for item in value:
        out.append(capo_iot.types.group_name_and_arn.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThingGroupNameAndArnList:
    import capo_iot.types.group_name_and_arn

    out: ThingGroupNameAndArnList = []
    for item in data:
        out.append(capo_iot.types.group_name_and_arn.deserialize_json(item))
    return out
