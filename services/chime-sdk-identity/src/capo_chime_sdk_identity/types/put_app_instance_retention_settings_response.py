"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#PutAppInstanceRetentionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_retention_settings
    import capo_chime_sdk_identity.types.timestamp


class PutAppInstanceRetentionSettingsResponse(TypedDict, closed=True):
    app_instance_retention_settings: NotRequired[
        "capo_chime_sdk_identity.types.app_instance_retention_settings.AppInstanceRetentionSettings"
    ]
    """<p>The time in days to retain data. Data type: number.</p>"""
    initiate_deletion_timestamp: NotRequired[
        "capo_chime_sdk_identity.types.timestamp.Timestamp"
    ]
    """<p>The time at which the API deletes data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAppInstanceRetentionSettingsResponse) -> dict:
    out: dict = {}
    if "app_instance_retention_settings" in value:
        import capo_chime_sdk_identity.types.app_instance_retention_settings

        out["AppInstanceRetentionSettings"] = (
            capo_chime_sdk_identity.types.app_instance_retention_settings.serialize_json(
                value["app_instance_retention_settings"]
            )
        )
    if "initiate_deletion_timestamp" in value:
        import capo_chime_sdk_identity.types.timestamp

        out["InitiateDeletionTimestamp"] = (
            capo_chime_sdk_identity.types.timestamp.serialize_json(
                value["initiate_deletion_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutAppInstanceRetentionSettingsResponse:
    out: PutAppInstanceRetentionSettingsResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceRetentionSettings" in data:
        import capo_chime_sdk_identity.types.app_instance_retention_settings

        out["app_instance_retention_settings"] = (
            capo_chime_sdk_identity.types.app_instance_retention_settings.deserialize_json(
                data["AppInstanceRetentionSettings"]
            )
        )
    if "InitiateDeletionTimestamp" in data:
        import capo_chime_sdk_identity.types.timestamp

        out["initiate_deletion_timestamp"] = (
            capo_chime_sdk_identity.types.timestamp.deserialize_json(
                data["InitiateDeletionTimestamp"]
            )
        )
    return out
