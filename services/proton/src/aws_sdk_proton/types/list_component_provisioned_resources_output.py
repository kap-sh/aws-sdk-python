"""Generated from Smithy shape ``com.amazonaws.proton#ListComponentProvisionedResourcesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.empty_next_token
    import aws_sdk_proton.types.provisioned_resource_list


class ListComponentProvisionedResourcesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the current requested list of provisioned resources.</p>"""
    provisioned_resources: (
        "aws_sdk_proton.types.provisioned_resource_list.ProvisionedResourceList"
    )
    """<p>An array of provisioned resources for a component.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListComponentProvisionedResourcesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_proton.types.provisioned_resource_list

    out["provisionedResources"] = (
        aws_sdk_proton.types.provisioned_resource_list.serialize_aws_json_1_0(
            value["provisioned_resources"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListComponentProvisionedResourcesOutput:
    out: ListComponentProvisionedResourcesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "provisionedResources" in data:
        import aws_sdk_proton.types.provisioned_resource_list

        out["provisioned_resources"] = (
            aws_sdk_proton.types.provisioned_resource_list.deserialize_aws_json_1_0(
                data["provisionedResources"]
            )
        )
    else:
        raise DeserializationError(
            "ListComponentProvisionedResourcesOutput.provisioned_resources required"
        )
    return out
