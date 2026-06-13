"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#LocationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.location_configuration

LocationConfigurations: TypeAlias = list[
    "aws_sdk_gameliftstreams.types.location_configuration.LocationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: LocationConfigurations) -> list:
    import aws_sdk_gameliftstreams.types.location_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gameliftstreams.types.location_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LocationConfigurations:
    import aws_sdk_gameliftstreams.types.location_configuration

    out: LocationConfigurations = []
    for item in data:
        out.append(
            aws_sdk_gameliftstreams.types.location_configuration.deserialize_json(item)
        )
    return out
