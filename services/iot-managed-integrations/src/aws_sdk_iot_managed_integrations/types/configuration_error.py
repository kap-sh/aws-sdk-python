"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConfigurationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.configuration_error_code
    import aws_sdk_iot_managed_integrations.types.configuration_error_message


class ConfigurationError(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_iot_managed_integrations.types.configuration_error_code.ConfigurationErrorCode"
    ]
    """<p>The error code returned when the default encryption configuration update fails.</p>"""
    message: NotRequired[
        "aws_sdk_iot_managed_integrations.types.configuration_error_message.ConfigurationErrorMessage"
    ]
    """<p>The error message returned when the default encryption configuration update fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationError) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConfigurationError:
    out: ConfigurationError = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
