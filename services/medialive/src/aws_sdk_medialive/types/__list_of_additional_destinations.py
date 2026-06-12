"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfAdditionalDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.additional_destinations

__listOfAdditionalDestinations: TypeAlias = list[
    "aws_sdk_medialive.types.additional_destinations.AdditionalDestinations"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAdditionalDestinations) -> list:
    import aws_sdk_medialive.types.additional_destinations

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.additional_destinations.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAdditionalDestinations:
    import aws_sdk_medialive.types.additional_destinations

    out: __listOfAdditionalDestinations = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.additional_destinations.deserialize_json(item)
        )
    return out
