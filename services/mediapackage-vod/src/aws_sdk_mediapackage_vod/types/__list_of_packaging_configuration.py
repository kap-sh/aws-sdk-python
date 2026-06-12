"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#__listOfPackagingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.packaging_configuration

__listOfPackagingConfiguration: TypeAlias = list[
    "aws_sdk_mediapackage_vod.types.packaging_configuration.PackagingConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPackagingConfiguration) -> list:
    import aws_sdk_mediapackage_vod.types.packaging_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackage_vod.types.packaging_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfPackagingConfiguration:
    import aws_sdk_mediapackage_vod.types.packaging_configuration

    out: __listOfPackagingConfiguration = []
    for item in data:
        out.append(
            aws_sdk_mediapackage_vod.types.packaging_configuration.deserialize_json(
                item
            )
        )
    return out
