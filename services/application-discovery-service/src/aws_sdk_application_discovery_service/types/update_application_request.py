"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.application_description
    import aws_sdk_application_discovery_service.types.application_id
    import aws_sdk_application_discovery_service.types.application_name
    import aws_sdk_application_discovery_service.types.application_wave


class UpdateApplicationRequest(TypedDict, closed=True):
    configuration_id: (
        "aws_sdk_application_discovery_service.types.application_id.ApplicationId"
    )
    """<p>Configuration ID of the application to be updated.</p>"""
    name: NotRequired[
        "aws_sdk_application_discovery_service.types.application_name.ApplicationName"
    ]
    """<p>New name of the application to be updated.</p>"""
    description: NotRequired[
        "aws_sdk_application_discovery_service.types.application_description.ApplicationDescription"
    ]
    """<p>New description of the application to be updated.</p>"""
    wave: NotRequired[
        "aws_sdk_application_discovery_service.types.application_wave.ApplicationWave"
    ]
    """<p>The new migration wave of the application that you want to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    out["configurationId"] = value["configuration_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "wave" in value:
        out["wave"] = value["wave"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    else:
        raise DeserializationError("UpdateApplicationRequest.configuration_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "wave" in data:
        out["wave"] = data["wave"]
    return out
