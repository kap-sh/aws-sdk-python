"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#GetAppInstanceRetentionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_retention_settings
    import aws_sdk_chime_sdk_identity.types.timestamp


class GetAppInstanceRetentionSettingsResponse(TypedDict, closed=True):
    app_instance_retention_settings: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance_retention_settings.AppInstanceRetentionSettings"
    ]
    """<p>The retention settings for the <code>AppInstance</code>.</p>"""
    initiate_deletion_timestamp: NotRequired[
        "aws_sdk_chime_sdk_identity.types.timestamp.Timestamp"
    ]
    """<p>The timestamp representing the time at which the specified items are retained, in Epoch Seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppInstanceRetentionSettingsResponse) -> dict:
    out: dict = {}
    if "app_instance_retention_settings" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance_retention_settings

        out["AppInstanceRetentionSettings"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_retention_settings.serialize_json(
                value["app_instance_retention_settings"]
            )
        )
    if "initiate_deletion_timestamp" in value:
        import aws_sdk_chime_sdk_identity.types.timestamp

        out["InitiateDeletionTimestamp"] = (
            aws_sdk_chime_sdk_identity.types.timestamp.serialize_json(
                value["initiate_deletion_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAppInstanceRetentionSettingsResponse:
    out: GetAppInstanceRetentionSettingsResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceRetentionSettings" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_retention_settings

        out["app_instance_retention_settings"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_retention_settings.deserialize_json(
                data["AppInstanceRetentionSettings"]
            )
        )
    if "InitiateDeletionTimestamp" in data:
        import aws_sdk_chime_sdk_identity.types.timestamp

        out["initiate_deletion_timestamp"] = (
            aws_sdk_chime_sdk_identity.types.timestamp.deserialize_json(
                data["InitiateDeletionTimestamp"]
            )
        )
    return out
