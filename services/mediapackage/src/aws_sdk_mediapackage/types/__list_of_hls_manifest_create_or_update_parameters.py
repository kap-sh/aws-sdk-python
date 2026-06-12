"""Generated from Smithy shape ``com.amazonaws.mediapackage#__listOfHlsManifestCreateOrUpdateParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.hls_manifest_create_or_update_parameters

__listOfHlsManifestCreateOrUpdateParameters: TypeAlias = list[
    "aws_sdk_mediapackage.types.hls_manifest_create_or_update_parameters.HlsManifestCreateOrUpdateParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHlsManifestCreateOrUpdateParameters) -> list:
    import aws_sdk_mediapackage.types.hls_manifest_create_or_update_parameters

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackage.types.hls_manifest_create_or_update_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfHlsManifestCreateOrUpdateParameters:
    import aws_sdk_mediapackage.types.hls_manifest_create_or_update_parameters

    out: __listOfHlsManifestCreateOrUpdateParameters = []
    for item in data:
        out.append(
            aws_sdk_mediapackage.types.hls_manifest_create_or_update_parameters.deserialize_json(
                item
            )
        )
    return out
