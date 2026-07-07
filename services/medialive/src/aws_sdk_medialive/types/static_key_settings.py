"""Generated from Smithy shape ``com.amazonaws.medialive#StaticKeySettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string_min32_max32
    import aws_sdk_medialive.types.input_location


class StaticKeySettings(TypedDict, closed=True):
    key_provider_server: NotRequired[
        "aws_sdk_medialive.types.input_location.InputLocation"
    ]
    """The URL of the license server used for protecting content."""
    static_key_value: NotRequired[
        "aws_sdk_medialive.types.__string_min32_max32.__stringMin32Max32"
    ]
    """Static key value as a 32 character hexadecimal string."""


# --- restJson1 ser/de ---
def serialize_json(value: StaticKeySettings) -> dict:
    out: dict = {}
    if "key_provider_server" in value:
        import aws_sdk_medialive.types.input_location

        out["keyProviderServer"] = (
            aws_sdk_medialive.types.input_location.serialize_json(
                value["key_provider_server"]
            )
        )
    if "static_key_value" in value:
        out["staticKeyValue"] = value["static_key_value"]
    return out


def deserialize_json(data: dict) -> StaticKeySettings:
    out: StaticKeySettings = {}  # type: ignore[typeddict-item]
    if "keyProviderServer" in data:
        import aws_sdk_medialive.types.input_location

        out["key_provider_server"] = (
            aws_sdk_medialive.types.input_location.deserialize_json(
                data["keyProviderServer"]
            )
        )
    if "staticKeyValue" in data:
        out["static_key_value"] = data["staticKeyValue"]
    return out
