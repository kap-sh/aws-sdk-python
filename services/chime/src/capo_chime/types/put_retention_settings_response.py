"""Generated from Smithy shape ``com.amazonaws.chime#PutRetentionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.iso8601_timestamp
    import capo_chime.types.retention_settings


class PutRetentionSettingsResponse(TypedDict, closed=True):
    retention_settings: NotRequired[
        "capo_chime.types.retention_settings.RetentionSettings"
    ]
    """<p>The retention settings.</p>"""
    initiate_deletion_timestamp: NotRequired[
        "capo_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The timestamp representing the time at which the specified items are permanently deleted, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRetentionSettingsResponse) -> dict:
    out: dict = {}
    if "retention_settings" in value:
        import capo_chime.types.retention_settings

        out["RetentionSettings"] = capo_chime.types.retention_settings.serialize_json(
            value["retention_settings"]
        )
    if "initiate_deletion_timestamp" in value:
        import capo_chime.types.iso8601_timestamp

        out["InitiateDeletionTimestamp"] = (
            capo_chime.types.iso8601_timestamp.serialize_json(
                value["initiate_deletion_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutRetentionSettingsResponse:
    out: PutRetentionSettingsResponse = {}  # type: ignore[typeddict-item]
    if "RetentionSettings" in data:
        import capo_chime.types.retention_settings

        out["retention_settings"] = (
            capo_chime.types.retention_settings.deserialize_json(
                data["RetentionSettings"]
            )
        )
    if "InitiateDeletionTimestamp" in data:
        import capo_chime.types.iso8601_timestamp

        out["initiate_deletion_timestamp"] = (
            capo_chime.types.iso8601_timestamp.deserialize_json(
                data["InitiateDeletionTimestamp"]
            )
        )
    return out
