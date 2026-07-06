"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeletionWarning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configuration_id
    import aws_sdk_application_discovery_service.types.warning_code
    import aws_sdk_application_discovery_service.types.warning_text


class DeletionWarning(TypedDict, closed=True):
    configuration_id: NotRequired[
        "aws_sdk_application_discovery_service.types.configuration_id.ConfigurationId"
    ]
    """<p> The unique identifier of the configuration that produced a warning. </p>"""
    warning_code: "aws_sdk_application_discovery_service.types.warning_code.WarningCode"
    """<p> The integer warning code associated with the warning message. </p>"""
    warning_text: NotRequired[
        "aws_sdk_application_discovery_service.types.warning_text.WarningText"
    ]
    """<p> A descriptive message of the warning the associated configuration ID produced. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletionWarning) -> dict:
    out: dict = {}
    if "configuration_id" in value:
        out["configurationId"] = value["configuration_id"]
    out["warningCode"] = value.get("warning_code", 0)
    if "warning_text" in value:
        out["warningText"] = value["warning_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletionWarning:
    out: DeletionWarning = {}  # type: ignore[typeddict-item]
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    if "warningCode" in data:
        out["warning_code"] = data["warningCode"]
    else:
        out["warning_code"] = 0
    if "warningText" in data:
        out["warning_text"] = data["warningText"]
    return out
