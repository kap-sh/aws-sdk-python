"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListWorkspaceInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.max_results
    import aws_sdk_workspaces_instances.types.next_token
    import aws_sdk_workspaces_instances.types.provision_states


class ListWorkspaceInstancesRequest(TypedDict):
    provision_states: NotRequired[
        "aws_sdk_workspaces_instances.types.provision_states.ProvisionStates"
    ]
    """<p>Filter WorkSpaces Instances by their current provisioning states.</p>"""
    max_results: NotRequired[
        "aws_sdk_workspaces_instances.types.max_results.MaxResults"
    ]
    """<p>Maximum number of WorkSpaces Instances to return in a single response.</p>"""
    next_token: NotRequired["aws_sdk_workspaces_instances.types.next_token.NextToken"]
    """<p>Pagination token for retrieving subsequent pages of WorkSpaces Instances.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkspaceInstancesRequest) -> dict:
    out: dict = {}
    if "provision_states" in value:
        import aws_sdk_workspaces_instances.types.provision_states

        out["ProvisionStates"] = (
            aws_sdk_workspaces_instances.types.provision_states.serialize_aws_json_1_0(
                value["provision_states"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkspaceInstancesRequest:
    out: ListWorkspaceInstancesRequest = {}  # type: ignore[typeddict-item]
    if "ProvisionStates" in data:
        import aws_sdk_workspaces_instances.types.provision_states

        out["provision_states"] = (
            aws_sdk_workspaces_instances.types.provision_states.deserialize_aws_json_1_0(
                data["ProvisionStates"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
