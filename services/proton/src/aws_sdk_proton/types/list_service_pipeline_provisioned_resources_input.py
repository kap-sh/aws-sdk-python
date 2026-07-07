"""Generated from Smithy shape ``com.amazonaws.proton#ListServicePipelineProvisionedResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.empty_next_token
    import aws_sdk_proton.types.resource_name


class ListServicePipelineProvisionedResourcesInput(TypedDict, closed=True):
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service whose pipeline's provisioned resources you want.</p>"""
    next_token: NotRequired["aws_sdk_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServicePipelineProvisionedResourcesInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListServicePipelineProvisionedResourcesInput:
    out: ListServicePipelineProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError(
            "ListServicePipelineProvisionedResourcesInput.service_name required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
