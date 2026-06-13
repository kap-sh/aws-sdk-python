"""Generated from Smithy shape ``com.amazonaws.repostspace#SpacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.space_data

SpacesList: TypeAlias = list["aws_sdk_repostspace.types.space_data.SpaceData"]


# --- restJson1 ser/de ---
def serialize_json(value: SpacesList) -> list:
    import aws_sdk_repostspace.types.space_data

    out: list = []
    for item in value:
        out.append(aws_sdk_repostspace.types.space_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpacesList:
    import aws_sdk_repostspace.types.space_data

    out: SpacesList = []
    for item in data:
        out.append(aws_sdk_repostspace.types.space_data.deserialize_json(item))
    return out
