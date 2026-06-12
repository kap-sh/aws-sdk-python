"""Generated from Smithy shape ``com.amazonaws.connect#Groupings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.grouping

Groupings: TypeAlias = list["aws_sdk_connect.types.grouping.Grouping"]


# --- restJson1 ser/de ---
def serialize_json(value: Groupings) -> list:
    import aws_sdk_connect.types.grouping

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.grouping.serialize_json(item))
    return out


def deserialize_json(data: list) -> Groupings:
    import aws_sdk_connect.types.grouping

    out: Groupings = []
    for item in data:
        out.append(aws_sdk_connect.types.grouping.deserialize_json(item))
    return out
