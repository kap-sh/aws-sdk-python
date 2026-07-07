"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppMessageButton``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.default_button_configuration
    import aws_sdk_pinpoint.types.override_button_configuration


class InAppMessageButton(TypedDict, closed=True):
    android: NotRequired[
        "aws_sdk_pinpoint.types.override_button_configuration.OverrideButtonConfiguration"
    ]
    """<p>Default button content.</p>"""
    default_config: NotRequired[
        "aws_sdk_pinpoint.types.default_button_configuration.DefaultButtonConfiguration"
    ]
    """<p>Default button content.</p>"""
    ios: NotRequired[
        "aws_sdk_pinpoint.types.override_button_configuration.OverrideButtonConfiguration"
    ]
    """<p>Default button content.</p>"""
    web: NotRequired[
        "aws_sdk_pinpoint.types.override_button_configuration.OverrideButtonConfiguration"
    ]
    """<p>Default button content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppMessageButton) -> dict:
    out: dict = {}
    if "android" in value:
        import aws_sdk_pinpoint.types.override_button_configuration

        out["Android"] = (
            aws_sdk_pinpoint.types.override_button_configuration.serialize_json(
                value["android"]
            )
        )
    if "default_config" in value:
        import aws_sdk_pinpoint.types.default_button_configuration

        out["DefaultConfig"] = (
            aws_sdk_pinpoint.types.default_button_configuration.serialize_json(
                value["default_config"]
            )
        )
    if "ios" in value:
        import aws_sdk_pinpoint.types.override_button_configuration

        out["IOS"] = (
            aws_sdk_pinpoint.types.override_button_configuration.serialize_json(
                value["ios"]
            )
        )
    if "web" in value:
        import aws_sdk_pinpoint.types.override_button_configuration

        out["Web"] = (
            aws_sdk_pinpoint.types.override_button_configuration.serialize_json(
                value["web"]
            )
        )
    return out


def deserialize_json(data: dict) -> InAppMessageButton:
    out: InAppMessageButton = {}  # type: ignore[typeddict-item]
    if "Android" in data:
        import aws_sdk_pinpoint.types.override_button_configuration

        out["android"] = (
            aws_sdk_pinpoint.types.override_button_configuration.deserialize_json(
                data["Android"]
            )
        )
    if "DefaultConfig" in data:
        import aws_sdk_pinpoint.types.default_button_configuration

        out["default_config"] = (
            aws_sdk_pinpoint.types.default_button_configuration.deserialize_json(
                data["DefaultConfig"]
            )
        )
    if "IOS" in data:
        import aws_sdk_pinpoint.types.override_button_configuration

        out["ios"] = (
            aws_sdk_pinpoint.types.override_button_configuration.deserialize_json(
                data["IOS"]
            )
        )
    if "Web" in data:
        import aws_sdk_pinpoint.types.override_button_configuration

        out["web"] = (
            aws_sdk_pinpoint.types.override_button_configuration.deserialize_json(
                data["Web"]
            )
        )
    return out
