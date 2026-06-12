"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeUserGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.user_group_list


class DescribeUserGroupsResult(TypedDict):
    user_groups: NotRequired["aws_sdk_elasticache.types.user_group_list.UserGroupList"]
    """<p>Returns a list of user groups.</p>"""
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeUserGroupsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_groups" in value:
        import aws_sdk_elasticache.types.user_group_list

        aws_sdk_elasticache.types.user_group_list.serialize_query(
            value["user_groups"], pairs, f"{prefix}.UserGroups"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeUserGroupsResult:
    out: DescribeUserGroupsResult = {}  # type: ignore[typeddict-item]
    child_user_groups = el.find("UserGroups")
    if child_user_groups is not None:
        import aws_sdk_elasticache.types.user_group_list

        out["user_groups"] = (
            aws_sdk_elasticache.types.user_group_list.deserialize_query(
                child_user_groups
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
