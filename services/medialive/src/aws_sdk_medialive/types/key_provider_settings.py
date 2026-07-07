"""Generated from Smithy shape ``com.amazonaws.medialive#KeyProviderSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.static_key_settings


class KeyProviderSettings(TypedDict, closed=True):
    static_key_settings: NotRequired[
        "aws_sdk_medialive.types.static_key_settings.StaticKeySettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: KeyProviderSettings) -> dict:
    out: dict = {}
    if "static_key_settings" in value:
        import aws_sdk_medialive.types.static_key_settings

        out["staticKeySettings"] = (
            aws_sdk_medialive.types.static_key_settings.serialize_json(
                value["static_key_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> KeyProviderSettings:
    out: KeyProviderSettings = {}  # type: ignore[typeddict-item]
    if "staticKeySettings" in data:
        import aws_sdk_medialive.types.static_key_settings

        out["static_key_settings"] = (
            aws_sdk_medialive.types.static_key_settings.deserialize_json(
                data["staticKeySettings"]
            )
        )
    return out
