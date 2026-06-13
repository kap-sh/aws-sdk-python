"""Generated from Smithy shape ``com.amazonaws.datazone#MatchOffsets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.match_offset

MatchOffsets: TypeAlias = list["aws_sdk_datazone.types.match_offset.MatchOffset"]


# --- restJson1 ser/de ---
def serialize_json(value: MatchOffsets) -> list:
    import aws_sdk_datazone.types.match_offset

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.match_offset.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchOffsets:
    import aws_sdk_datazone.types.match_offset

    out: MatchOffsets = []
    for item in data:
        out.append(aws_sdk_datazone.types.match_offset.deserialize_json(item))
    return out
