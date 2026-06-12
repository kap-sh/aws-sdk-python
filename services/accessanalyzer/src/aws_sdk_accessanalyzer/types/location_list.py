"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#LocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.location

LocationList: TypeAlias = list["aws_sdk_accessanalyzer.types.location.Location"]


# --- restJson1 ser/de ---
def serialize_json(value: LocationList) -> list:
    import aws_sdk_accessanalyzer.types.location

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.location.serialize_json(item))
    return out


def deserialize_json(data: list) -> LocationList:
    import aws_sdk_accessanalyzer.types.location

    out: LocationList = []
    for item in data:
        out.append(aws_sdk_accessanalyzer.types.location.deserialize_json(item))
    return out
