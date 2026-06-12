"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfRouterDestinationSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.router_destination_settings

__listOfRouterDestinationSettings: TypeAlias = list[
    "aws_sdk_medialive.types.router_destination_settings.RouterDestinationSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRouterDestinationSettings) -> list:
    import aws_sdk_medialive.types.router_destination_settings

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.router_destination_settings.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfRouterDestinationSettings:
    import aws_sdk_medialive.types.router_destination_settings

    out: __listOfRouterDestinationSettings = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.router_destination_settings.deserialize_json(item)
        )
    return out
