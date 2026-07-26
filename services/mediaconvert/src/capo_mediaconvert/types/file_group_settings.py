"""Generated from Smithy shape ``com.amazonaws.mediaconvert#FileGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_pattern_s3
    import capo_mediaconvert.types.destination_settings


class FileGroupSettings(TypedDict, closed=True):
    destination: NotRequired[
        "capo_mediaconvert.types.__string_pattern_s3.__stringPatternS3"
    ]
    """Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file."""
    destination_settings: NotRequired[
        "capo_mediaconvert.types.destination_settings.DestinationSettings"
    ]
    """Settings associated with the destination. Will vary based on the type of destination"""


# --- restJson1 ser/de ---
def serialize_json(value: FileGroupSettings) -> dict:
    out: dict = {}
    if "destination" in value:
        out["destination"] = value["destination"]
    if "destination_settings" in value:
        import capo_mediaconvert.types.destination_settings

        out["destinationSettings"] = (
            capo_mediaconvert.types.destination_settings.serialize_json(
                value["destination_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FileGroupSettings:
    out: FileGroupSettings = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        out["destination"] = data["destination"]
    if "destinationSettings" in data:
        import capo_mediaconvert.types.destination_settings

        out["destination_settings"] = (
            capo_mediaconvert.types.destination_settings.deserialize_json(
                data["destinationSettings"]
            )
        )
    return out
