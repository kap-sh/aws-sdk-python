"""Generated from Smithy shape ``com.amazonaws.dlm#ResourceLocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.resource_location_values

ResourceLocationList: TypeAlias = list[
    "aws_sdk_dlm.types.resource_location_values.ResourceLocationValues"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLocationList) -> list:
    import aws_sdk_dlm.types.resource_location_values

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.resource_location_values.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceLocationList:
    import aws_sdk_dlm.types.resource_location_values

    out: ResourceLocationList = []
    for item in data:
        out.append(aws_sdk_dlm.types.resource_location_values.deserialize_json(item))
    return out
