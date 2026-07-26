"""Generated from Smithy shape ``com.amazonaws.medialive#ArchiveCdnSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.archive_s3_settings


class ArchiveCdnSettings(TypedDict, closed=True):
    archive_s3_settings: NotRequired[
        "capo_medialive.types.archive_s3_settings.ArchiveS3Settings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveCdnSettings) -> dict:
    out: dict = {}
    if "archive_s3_settings" in value:
        import capo_medialive.types.archive_s3_settings

        out["archiveS3Settings"] = (
            capo_medialive.types.archive_s3_settings.serialize_json(
                value["archive_s3_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ArchiveCdnSettings:
    out: ArchiveCdnSettings = {}  # type: ignore[typeddict-item]
    if "archiveS3Settings" in data:
        import capo_medialive.types.archive_s3_settings

        out["archive_s3_settings"] = (
            capo_medialive.types.archive_s3_settings.deserialize_json(
                data["archiveS3Settings"]
            )
        )
    return out
