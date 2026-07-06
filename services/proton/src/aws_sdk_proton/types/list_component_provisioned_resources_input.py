"""Generated from Smithy shape ``com.amazonaws.proton#ListComponentProvisionedResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.empty_next_token
    import aws_sdk_proton.types.resource_name


class ListComponentProvisionedResourcesInput(TypedDict, closed=True):
    component_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the component whose provisioned resources you want.</p>"""
    next_token: NotRequired["aws_sdk_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListComponentProvisionedResourcesInput) -> dict:
    out: dict = {}
    out["componentName"] = value["component_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListComponentProvisionedResourcesInput:
    out: ListComponentProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    else:
        raise DeserializationError(
            "ListComponentProvisionedResourcesInput.component_name required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
