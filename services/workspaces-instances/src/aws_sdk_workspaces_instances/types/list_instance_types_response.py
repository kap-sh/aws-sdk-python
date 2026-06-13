"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListInstanceTypesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.instance_types
    import aws_sdk_workspaces_instances.types.next_token


class ListInstanceTypesResponse(TypedDict):
    instance_types: "aws_sdk_workspaces_instances.types.instance_types.InstanceTypes"
    """<p>Collection of supported instance types for WorkSpaces Instances.</p>"""
    next_token: NotRequired["aws_sdk_workspaces_instances.types.next_token.NextToken"]
    """<p>Token for retrieving additional instance types if the result set is paginated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInstanceTypesResponse) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_instances.types.instance_types

    out["InstanceTypes"] = (
        aws_sdk_workspaces_instances.types.instance_types.serialize_aws_json_1_0(
            value["instance_types"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInstanceTypesResponse:
    out: ListInstanceTypesResponse = {}  # type: ignore[typeddict-item]
    if "InstanceTypes" in data:
        import aws_sdk_workspaces_instances.types.instance_types

        out["instance_types"] = (
            aws_sdk_workspaces_instances.types.instance_types.deserialize_aws_json_1_0(
                data["InstanceTypes"]
            )
        )
    else:
        raise DeserializationError("ListInstanceTypesResponse.instance_types required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
