"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#TrailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.trail

TrailList: TypeAlias = list["aws_sdk_accessanalyzer.types.trail.Trail"]


# --- restJson1 ser/de ---
def serialize_json(value: TrailList) -> list:
    import aws_sdk_accessanalyzer.types.trail

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.trail.serialize_json(item))
    return out


def deserialize_json(data: list) -> TrailList:
    import aws_sdk_accessanalyzer.types.trail

    out: TrailList = []
    for item in data:
        out.append(aws_sdk_accessanalyzer.types.trail.deserialize_json(item))
    return out
