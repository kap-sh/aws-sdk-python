"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeContainerInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_instance_field_list
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class DescribeContainerInstancesRequest(TypedDict, closed=True):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the container instance or container instances you are describing were launched in any cluster other than the default cluster.</p>"""
    container_instances: "aws_sdk_ecs.types.string_list.StringList"
    """<p>A list of up to 100 container instance IDs or full Amazon Resource Name (ARN) entries.</p>"""
    include: NotRequired[
        "aws_sdk_ecs.types.container_instance_field_list.ContainerInstanceFieldList"
    ]
    """<p>Specifies whether you want to see the resource tags for the container instance. If <code>TAGS</code> is specified, the tags are included in the response. If <code>CONTAINER_INSTANCE_HEALTH</code> is specified, the container instance health is included in the response. If this field is omitted, tags and container instance health status aren't included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerInstancesRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    import aws_sdk_ecs.types.string_list

    out["containerInstances"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
        value["container_instances"]
    )
    if "include" in value:
        import aws_sdk_ecs.types.container_instance_field_list

        out["include"] = (
            aws_sdk_ecs.types.container_instance_field_list.serialize_aws_json_1_1(
                value["include"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerInstancesRequest:
    out: DescribeContainerInstancesRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "containerInstances" in data:
        import aws_sdk_ecs.types.string_list

        out["container_instances"] = (
            aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
                data["containerInstances"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeContainerInstancesRequest.container_instances required"
        )
    if "include" in data:
        import aws_sdk_ecs.types.container_instance_field_list

        out["include"] = (
            aws_sdk_ecs.types.container_instance_field_list.deserialize_aws_json_1_1(
                data["include"]
            )
        )
    return out
