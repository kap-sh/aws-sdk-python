"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#PutAppInstanceUserExpirationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.expiration_settings


class PutAppInstanceUserExpirationSettingsRequest(TypedDict, closed=True):
    app_instance_user_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    expiration_settings: NotRequired[
        "capo_chime_sdk_identity.types.expiration_settings.ExpirationSettings"
    ]
    """<p>Settings that control the interval after which an <code>AppInstanceUser</code> is automatically deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAppInstanceUserExpirationSettingsRequest) -> dict:
    out: dict = {}
    if "expiration_settings" in value:
        import capo_chime_sdk_identity.types.expiration_settings

        out["ExpirationSettings"] = (
            capo_chime_sdk_identity.types.expiration_settings.serialize_json(
                value["expiration_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutAppInstanceUserExpirationSettingsRequest:
    out: PutAppInstanceUserExpirationSettingsRequest = {}  # type: ignore[typeddict-item]
    if "ExpirationSettings" in data:
        import capo_chime_sdk_identity.types.expiration_settings

        out["expiration_settings"] = (
            capo_chime_sdk_identity.types.expiration_settings.deserialize_json(
                data["ExpirationSettings"]
            )
        )
    return out
