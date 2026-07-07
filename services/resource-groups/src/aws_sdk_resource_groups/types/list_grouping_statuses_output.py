"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupingStatusesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_string_v2
    import aws_sdk_resource_groups.types.grouping_statuses_list
    import aws_sdk_resource_groups.types.next_token


class ListGroupingStatusesOutput(TypedDict, closed=True):
    group: NotRequired["aws_sdk_resource_groups.types.group_string_v2.GroupStringV2"]
    """<p>The application group identifier, expressed as an Amazon resource name (ARN) or the application group name.</p>"""
    grouping_statuses: NotRequired[
        "aws_sdk_resource_groups.types.grouping_statuses_list.GroupingStatusesList"
    ]
    """<p>Returns details about the grouping or ungrouping status of the resources in the specified application group. </p>"""
    next_token: NotRequired["aws_sdk_resource_groups.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingStatusesOutput) -> dict:
    out: dict = {}
    if "group" in value:
        out["Group"] = value["group"]
    if "grouping_statuses" in value:
        import aws_sdk_resource_groups.types.grouping_statuses_list

        out["GroupingStatuses"] = (
            aws_sdk_resource_groups.types.grouping_statuses_list.serialize_json(
                value["grouping_statuses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupingStatusesOutput:
    out: ListGroupingStatusesOutput = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        out["group"] = data["Group"]
    if "GroupingStatuses" in data:
        import aws_sdk_resource_groups.types.grouping_statuses_list

        out["grouping_statuses"] = (
            aws_sdk_resource_groups.types.grouping_statuses_list.deserialize_json(
                data["GroupingStatuses"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
