"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTaskSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.task_set_field_list


class DescribeTaskSetsRequest(TypedDict, closed=True):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>"""
    service: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that the task sets exist in.</p>"""
    task_sets: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The ID or full Amazon Resource Name (ARN) of task sets to describe.</p>"""
    include: NotRequired["aws_sdk_ecs.types.task_set_field_list.TaskSetFieldList"]
    """<p>Specifies whether to see the resource tags for the task set. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTaskSetsRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    out["service"] = value["service"]
    if "task_sets" in value:
        import aws_sdk_ecs.types.string_list

        out["taskSets"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["task_sets"]
        )
    if "include" in value:
        import aws_sdk_ecs.types.task_set_field_list

        out["include"] = aws_sdk_ecs.types.task_set_field_list.serialize_aws_json_1_1(
            value["include"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTaskSetsRequest:
    out: DescribeTaskSetsRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    else:
        raise DeserializationError("DescribeTaskSetsRequest.cluster required")
    if "service" in data:
        out["service"] = data["service"]
    else:
        raise DeserializationError("DescribeTaskSetsRequest.service required")
    if "taskSets" in data:
        import aws_sdk_ecs.types.string_list

        out["task_sets"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["taskSets"]
        )
    if "include" in data:
        import aws_sdk_ecs.types.task_set_field_list

        out["include"] = aws_sdk_ecs.types.task_set_field_list.deserialize_aws_json_1_1(
            data["include"]
        )
    return out
