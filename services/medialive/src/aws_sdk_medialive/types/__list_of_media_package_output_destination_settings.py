"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMediaPackageOutputDestinationSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.media_package_output_destination_settings

__listOfMediaPackageOutputDestinationSettings: TypeAlias = list[
    "aws_sdk_medialive.types.media_package_output_destination_settings.MediaPackageOutputDestinationSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaPackageOutputDestinationSettings) -> list:
    import aws_sdk_medialive.types.media_package_output_destination_settings

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.media_package_output_destination_settings.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfMediaPackageOutputDestinationSettings:
    import aws_sdk_medialive.types.media_package_output_destination_settings

    out: __listOfMediaPackageOutputDestinationSettings = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.media_package_output_destination_settings.deserialize_json(
                item
            )
        )
    return out
