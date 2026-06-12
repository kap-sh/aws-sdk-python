"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListTagSyncTasksFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_arn_v2
    import aws_sdk_resource_groups.types.group_name


class ListTagSyncTasksFilter(TypedDict):
    group_arn: NotRequired["aws_sdk_resource_groups.types.group_arn_v2.GroupArnV2"]
    """<p>The Amazon resource name (ARN) of the application group. </p>"""
    group_name: NotRequired["aws_sdk_resource_groups.types.group_name.GroupName"]
    """<p>The name of the application group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagSyncTasksFilter) -> dict:
    out: dict = {}
    if "group_arn" in value:
        out["GroupArn"] = value["group_arn"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    return out


def deserialize_json(data: dict) -> ListTagSyncTasksFilter:
    out: ListTagSyncTasksFilter = {}  # type: ignore[typeddict-item]
    if "GroupArn" in data:
        out["group_arn"] = data["GroupArn"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    return out
