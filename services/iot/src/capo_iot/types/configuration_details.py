"""Generated from Smithy shape ``com.amazonaws.iot#ConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.configuration_status
    import capo_iot.types.error_code
    import capo_iot.types.error_message


class ConfigurationDetails(TypedDict, closed=True):
    configuration_status: NotRequired[
        "capo_iot.types.configuration_status.ConfigurationStatus"
    ]
    """<p>The health status of KMS key and KMS access role. If either KMS key or KMS access role is <code>UNHEALTHY</code>, the return value will be <code>UNHEALTHY</code>. To use a customer managed KMS key, the value of <code>configurationStatus</code> must be <code>HEALTHY</code>. </p>"""
    error_code: NotRequired["capo_iot.types.error_code.ErrorCode"]
    """<p>The error code that indicates either the KMS key or the KMS access role is <code>UNHEALTHY</code>. Valid values: <code>KMS_KEY_VALIDATION_ERROR</code> and <code>ROLE_VALIDATION_ERROR</code>. </p>"""
    error_message: NotRequired["capo_iot.types.error_message.ErrorMessage"]
    """<p>The detailed error message that corresponds to the <code>errorCode</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationDetails) -> dict:
    out: dict = {}
    if "configuration_status" in value:
        import capo_iot.types.configuration_status

        out["configurationStatus"] = capo_iot.types.configuration_status.serialize_json(
            value["configuration_status"]
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ConfigurationDetails:
    out: ConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "configurationStatus" in data:
        import capo_iot.types.configuration_status

        out["configuration_status"] = (
            capo_iot.types.configuration_status.deserialize_json(
                data["configurationStatus"]
            )
        )
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
