"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#PutAppInstanceUserExpirationSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.expiration_settings


class PutAppInstanceUserExpirationSettingsResponse(TypedDict):
    app_instance_user_arn: NotRequired[
        "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    expiration_settings: NotRequired[
        "aws_sdk_chime_sdk_identity.types.expiration_settings.ExpirationSettings"
    ]
    """<p>Settings that control the interval after which an <code>AppInstanceUser</code> is automatically deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAppInstanceUserExpirationSettingsResponse) -> dict:
    out: dict = {}
    if "app_instance_user_arn" in value:
        out["AppInstanceUserArn"] = value["app_instance_user_arn"]
    if "expiration_settings" in value:
        import aws_sdk_chime_sdk_identity.types.expiration_settings

        out["ExpirationSettings"] = (
            aws_sdk_chime_sdk_identity.types.expiration_settings.serialize_json(
                value["expiration_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutAppInstanceUserExpirationSettingsResponse:
    out: PutAppInstanceUserExpirationSettingsResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceUserArn" in data:
        out["app_instance_user_arn"] = data["AppInstanceUserArn"]
    if "ExpirationSettings" in data:
        import aws_sdk_chime_sdk_identity.types.expiration_settings

        out["expiration_settings"] = (
            aws_sdk_chime_sdk_identity.types.expiration_settings.deserialize_json(
                data["ExpirationSettings"]
            )
        )
    return out
