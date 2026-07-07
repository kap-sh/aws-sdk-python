"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.string


class CreateApplicationResponse(TypedDict, closed=True):
    configuration_id: NotRequired[
        "aws_sdk_application_discovery_service.types.string.String"
    ]
    """<p>The configuration ID of an application to be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    if "configuration_id" in value:
        out["configurationId"] = value["configuration_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    return out
