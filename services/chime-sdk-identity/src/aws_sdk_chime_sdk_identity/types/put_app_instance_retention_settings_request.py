"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#PutAppInstanceRetentionSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_retention_settings
    import aws_sdk_chime_sdk_identity.types.chime_arn


class PutAppInstanceRetentionSettingsRequest(TypedDict, closed=True):
    app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code>.</p>"""
    app_instance_retention_settings: "aws_sdk_chime_sdk_identity.types.app_instance_retention_settings.AppInstanceRetentionSettings"
    """<p>The time in days to retain data. Data type: number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAppInstanceRetentionSettingsRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_identity.types.app_instance_retention_settings

    out["AppInstanceRetentionSettings"] = (
        aws_sdk_chime_sdk_identity.types.app_instance_retention_settings.serialize_json(
            value["app_instance_retention_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutAppInstanceRetentionSettingsRequest:
    out: PutAppInstanceRetentionSettingsRequest = {}  # type: ignore[typeddict-item]
    if "AppInstanceRetentionSettings" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_retention_settings

        out["app_instance_retention_settings"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_retention_settings.deserialize_json(
                data["AppInstanceRetentionSettings"]
            )
        )
    else:
        raise DeserializationError(
            "PutAppInstanceRetentionSettingsRequest.app_instance_retention_settings required"
        )
    return out
