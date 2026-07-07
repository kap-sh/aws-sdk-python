"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.task_field_list


class DescribeTasksRequest(TypedDict, closed=True):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task or tasks to describe. If you do not specify a cluster, the default cluster is assumed.</p>"""
    tasks: "aws_sdk_ecs.types.string_list.StringList"
    """<p>A list of up to 100 task IDs or full ARN entries.</p>"""
    include: NotRequired["aws_sdk_ecs.types.task_field_list.TaskFieldList"]
    """<p>Specifies whether you want to see the resource tags for the task. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTasksRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    import aws_sdk_ecs.types.string_list

    out["tasks"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(value["tasks"])
    if "include" in value:
        import aws_sdk_ecs.types.task_field_list

        out["include"] = aws_sdk_ecs.types.task_field_list.serialize_aws_json_1_1(
            value["include"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTasksRequest:
    out: DescribeTasksRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "tasks" in data:
        import aws_sdk_ecs.types.string_list

        out["tasks"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["tasks"]
        )
    else:
        raise DeserializationError("DescribeTasksRequest.tasks required")
    if "include" in data:
        import aws_sdk_ecs.types.task_field_list

        out["include"] = aws_sdk_ecs.types.task_field_list.deserialize_aws_json_1_1(
            data["include"]
        )
    return out
