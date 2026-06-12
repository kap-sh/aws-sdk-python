"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMediaPackageAdditionalDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.media_package_additional_destinations

__listOfMediaPackageAdditionalDestinations: TypeAlias = list[
    "aws_sdk_medialive.types.media_package_additional_destinations.MediaPackageAdditionalDestinations"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaPackageAdditionalDestinations) -> list:
    import aws_sdk_medialive.types.media_package_additional_destinations

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.media_package_additional_destinations.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfMediaPackageAdditionalDestinations:
    import aws_sdk_medialive.types.media_package_additional_destinations

    out: __listOfMediaPackageAdditionalDestinations = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.media_package_additional_destinations.deserialize_json(
                item
            )
        )
    return out
