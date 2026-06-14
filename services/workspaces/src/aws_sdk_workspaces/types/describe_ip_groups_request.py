"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeIpGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ip_group_id_list
    import aws_sdk_workspaces.types.limit
    import aws_sdk_workspaces.types.pagination_token


class DescribeIpGroupsRequest(TypedDict):
    group_ids: NotRequired["aws_sdk_workspaces.types.ip_group_id_list.IpGroupIdList"]
    """<p>The identifiers of one or more IP access control groups.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_workspaces.types.limit.Limit"]
    """<p>The maximum number of items to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIpGroupsRequest) -> dict:
    out: dict = {}
    if "group_ids" in value:
        import aws_sdk_workspaces.types.ip_group_id_list

        out["GroupIds"] = (
            aws_sdk_workspaces.types.ip_group_id_list.serialize_aws_json_1_1(
                value["group_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIpGroupsRequest:
    out: DescribeIpGroupsRequest = {}  # type: ignore[typeddict-item]
    if "GroupIds" in data:
        import aws_sdk_workspaces.types.ip_group_id_list

        out["group_ids"] = (
            aws_sdk_workspaces.types.ip_group_id_list.deserialize_aws_json_1_1(
                data["GroupIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
