"""Generated from Smithy shape ``com.amazonaws.deadline#FarmMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_member

FarmMembers: TypeAlias = list["aws_sdk_deadline.types.farm_member.FarmMember"]


# --- restJson1 ser/de ---
def serialize_json(value: FarmMembers) -> list:
    import aws_sdk_deadline.types.farm_member

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.farm_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> FarmMembers:
    import aws_sdk_deadline.types.farm_member

    out: FarmMembers = []
    for item in data:
        out.append(aws_sdk_deadline.types.farm_member.deserialize_json(item))
    return out
