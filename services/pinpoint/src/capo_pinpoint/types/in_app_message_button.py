"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppMessageButton``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.default_button_configuration
    import capo_pinpoint.types.override_button_configuration


class InAppMessageButton(TypedDict, closed=True):
    android: NotRequired[
        "capo_pinpoint.types.override_button_configuration.OverrideButtonConfiguration"
    ]
    """<p>Default button content.</p>"""
    default_config: NotRequired[
        "capo_pinpoint.types.default_button_configuration.DefaultButtonConfiguration"
    ]
    """<p>Default button content.</p>"""
    ios: NotRequired[
        "capo_pinpoint.types.override_button_configuration.OverrideButtonConfiguration"
    ]
    """<p>Default button content.</p>"""
    web: NotRequired[
        "capo_pinpoint.types.override_button_configuration.OverrideButtonConfiguration"
    ]
    """<p>Default button content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppMessageButton) -> dict:
    out: dict = {}
    if "android" in value:
        import capo_pinpoint.types.override_button_configuration

        out["Android"] = (
            capo_pinpoint.types.override_button_configuration.serialize_json(
                value["android"]
            )
        )
    if "default_config" in value:
        import capo_pinpoint.types.default_button_configuration

        out["DefaultConfig"] = (
            capo_pinpoint.types.default_button_configuration.serialize_json(
                value["default_config"]
            )
        )
    if "ios" in value:
        import capo_pinpoint.types.override_button_configuration

        out["IOS"] = capo_pinpoint.types.override_button_configuration.serialize_json(
            value["ios"]
        )
    if "web" in value:
        import capo_pinpoint.types.override_button_configuration

        out["Web"] = capo_pinpoint.types.override_button_configuration.serialize_json(
            value["web"]
        )
    return out


def deserialize_json(data: dict) -> InAppMessageButton:
    out: InAppMessageButton = {}  # type: ignore[typeddict-item]
    if "Android" in data:
        import capo_pinpoint.types.override_button_configuration

        out["android"] = (
            capo_pinpoint.types.override_button_configuration.deserialize_json(
                data["Android"]
            )
        )
    if "DefaultConfig" in data:
        import capo_pinpoint.types.default_button_configuration

        out["default_config"] = (
            capo_pinpoint.types.default_button_configuration.deserialize_json(
                data["DefaultConfig"]
            )
        )
    if "IOS" in data:
        import capo_pinpoint.types.override_button_configuration

        out["ios"] = capo_pinpoint.types.override_button_configuration.deserialize_json(
            data["IOS"]
        )
    if "Web" in data:
        import capo_pinpoint.types.override_button_configuration

        out["web"] = capo_pinpoint.types.override_button_configuration.deserialize_json(
            data["Web"]
        )
    return out
