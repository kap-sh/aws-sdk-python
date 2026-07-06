"""Generated from Smithy shape ``com.amazonaws.ecs#ListContainerInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ListContainerInstancesResponse(TypedDict, closed=True):
    container_instance_arns: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of container instances with full ARN entries for each container instance associated with the specified cluster.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListContainerInstances</code> request. When the results of a <code>ListContainerInstances</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContainerInstancesResponse) -> dict:
    out: dict = {}
    if "container_instance_arns" in value:
        import aws_sdk_ecs.types.string_list

        out["containerInstanceArns"] = (
            aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
                value["container_instance_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContainerInstancesResponse:
    out: ListContainerInstancesResponse = {}  # type: ignore[typeddict-item]
    if "containerInstanceArns" in data:
        import aws_sdk_ecs.types.string_list

        out["container_instance_arns"] = (
            aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
                data["containerInstanceArns"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
