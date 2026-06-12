"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#TrailPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.trail_properties

TrailPropertiesList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.trail_properties.TrailProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrailPropertiesList) -> list:
    import aws_sdk_accessanalyzer.types.trail_properties

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.trail_properties.serialize_json(item))
    return out


def deserialize_json(data: list) -> TrailPropertiesList:
    import aws_sdk_accessanalyzer.types.trail_properties

    out: TrailPropertiesList = []
    for item in data:
        out.append(aws_sdk_accessanalyzer.types.trail_properties.deserialize_json(item))
    return out
