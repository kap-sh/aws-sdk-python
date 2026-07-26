"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeMediaStorageConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.media_storage_configuration


class DescribeMediaStorageConfigurationOutput(TypedDict, closed=True):
    media_storage_configuration: NotRequired[
        "capo_kinesis_video.types.media_storage_configuration.MediaStorageConfiguration"
    ]
    """<p>A structure that encapsulates, or contains, the media storage configuration properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMediaStorageConfigurationOutput) -> dict:
    out: dict = {}
    if "media_storage_configuration" in value:
        import capo_kinesis_video.types.media_storage_configuration

        out["MediaStorageConfiguration"] = (
            capo_kinesis_video.types.media_storage_configuration.serialize_json(
                value["media_storage_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeMediaStorageConfigurationOutput:
    out: DescribeMediaStorageConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "MediaStorageConfiguration" in data:
        import capo_kinesis_video.types.media_storage_configuration

        out["media_storage_configuration"] = (
            capo_kinesis_video.types.media_storage_configuration.deserialize_json(
                data["MediaStorageConfiguration"]
            )
        )
    return out
