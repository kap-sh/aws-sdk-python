"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.s3_destination_settings


class DestinationSettings(TypedDict, closed=True):
    s3_settings: NotRequired[
        "aws_sdk_mediaconvert.types.s3_destination_settings.S3DestinationSettings"
    ]
    """Settings associated with S3 destination"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationSettings) -> dict:
    out: dict = {}
    if "s3_settings" in value:
        import aws_sdk_mediaconvert.types.s3_destination_settings

        out["s3Settings"] = (
            aws_sdk_mediaconvert.types.s3_destination_settings.serialize_json(
                value["s3_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationSettings:
    out: DestinationSettings = {}  # type: ignore[typeddict-item]
    if "s3Settings" in data:
        import aws_sdk_mediaconvert.types.s3_destination_settings

        out["s3_settings"] = (
            aws_sdk_mediaconvert.types.s3_destination_settings.deserialize_json(
                data["s3Settings"]
            )
        )
    return out
