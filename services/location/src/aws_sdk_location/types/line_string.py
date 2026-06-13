"""Generated from Smithy shape ``com.amazonaws.location#LineString``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.position

LineString: TypeAlias = list["aws_sdk_location.types.position.Position"]


# --- restJson1 ser/de ---
def serialize_json(value: LineString) -> list:
    import aws_sdk_location.types.position

    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.position.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineString:
    import aws_sdk_location.types.position

    out: LineString = []
    for item in data:
        out.append(aws_sdk_location.types.position.deserialize_json(item))
    return out
