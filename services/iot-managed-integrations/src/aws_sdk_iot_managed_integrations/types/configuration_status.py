"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConfigurationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.configuration_error
    import aws_sdk_iot_managed_integrations.types.configuration_state


class ConfigurationStatus(TypedDict, closed=True):
    error: NotRequired[
        "aws_sdk_iot_managed_integrations.types.configuration_error.ConfigurationError"
    ]
    """<p>The error details describing a failed default encryption configuration update.</p>"""
    state: (
        "aws_sdk_iot_managed_integrations.types.configuration_state.ConfigurationState"
    )
    """<p>The status state describing the default encryption configuration update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationStatus) -> dict:
    out: dict = {}
    if "error" in value:
        import aws_sdk_iot_managed_integrations.types.configuration_error

        out["error"] = (
            aws_sdk_iot_managed_integrations.types.configuration_error.serialize_json(
                value["error"]
            )
        )
    import aws_sdk_iot_managed_integrations.types.configuration_state

    out["state"] = (
        aws_sdk_iot_managed_integrations.types.configuration_state.serialize_json(
            value["state"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConfigurationStatus:
    out: ConfigurationStatus = {}  # type: ignore[typeddict-item]
    if "error" in data:
        import aws_sdk_iot_managed_integrations.types.configuration_error

        out["error"] = (
            aws_sdk_iot_managed_integrations.types.configuration_error.deserialize_json(
                data["error"]
            )
        )
    if "state" in data:
        import aws_sdk_iot_managed_integrations.types.configuration_state

        out["state"] = (
            aws_sdk_iot_managed_integrations.types.configuration_state.deserialize_json(
                data["state"]
            )
        )
    else:
        raise DeserializationError("ConfigurationStatus.state required")
    return out
