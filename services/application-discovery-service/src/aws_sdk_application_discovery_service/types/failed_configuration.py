"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#FailedConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configuration_id
    import aws_sdk_application_discovery_service.types.error_message
    import aws_sdk_application_discovery_service.types.error_status_code


class FailedConfiguration(TypedDict):
    configuration_id: NotRequired[
        "aws_sdk_application_discovery_service.types.configuration_id.ConfigurationId"
    ]
    """<p> The unique identifier of the configuration the failed to delete. </p>"""
    error_status_code: (
        "aws_sdk_application_discovery_service.types.error_status_code.ErrorStatusCode"
    )
    """<p> The integer error code associated with the error message. </p>"""
    error_message: NotRequired[
        "aws_sdk_application_discovery_service.types.error_message.ErrorMessage"
    ]
    """<p> A descriptive message indicating why the associated configuration failed to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedConfiguration) -> dict:
    out: dict = {}
    if "configuration_id" in value:
        out["configurationId"] = value["configuration_id"]
    out["errorStatusCode"] = value.get("error_status_code", 0)
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedConfiguration:
    out: FailedConfiguration = {}  # type: ignore[typeddict-item]
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    if "errorStatusCode" in data:
        out["error_status_code"] = data["errorStatusCode"]
    else:
        out["error_status_code"] = 0
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
