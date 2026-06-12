"""Generated from Smithy shape ``com.amazonaws.medialive#ArchiveCdnSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.archive_s3_settings


class ArchiveCdnSettings(TypedDict):
    archive_s3_settings: NotRequired[
        "aws_sdk_medialive.types.archive_s3_settings.ArchiveS3Settings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveCdnSettings) -> dict:
    out: dict = {}
    if "archive_s3_settings" in value:
        import aws_sdk_medialive.types.archive_s3_settings

        out["archiveS3Settings"] = (
            aws_sdk_medialive.types.archive_s3_settings.serialize_json(
                value["archive_s3_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ArchiveCdnSettings:
    out: ArchiveCdnSettings = {}  # type: ignore[typeddict-item]
    if "archiveS3Settings" in data:
        import aws_sdk_medialive.types.archive_s3_settings

        out["archive_s3_settings"] = (
            aws_sdk_medialive.types.archive_s3_settings.deserialize_json(
                data["archiveS3Settings"]
            )
        )
    return out
