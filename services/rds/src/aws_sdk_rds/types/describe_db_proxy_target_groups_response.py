"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBProxyTargetGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.target_group_list


class DescribeDBProxyTargetGroupsResponse(TypedDict, closed=True):
    target_groups: NotRequired["aws_sdk_rds.types.target_group_list.TargetGroupList"]
    """<p>An arbitrary number of <code>DBProxyTargetGroup</code> objects, containing details of the corresponding target groups.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBProxyTargetGroupsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "target_groups" in value:
        import aws_sdk_rds.types.target_group_list

        aws_sdk_rds.types.target_group_list.serialize_query(
            value["target_groups"], pairs, f"{prefix}.TargetGroups"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBProxyTargetGroupsResponse:
    out: DescribeDBProxyTargetGroupsResponse = {}  # type: ignore[typeddict-item]
    child_target_groups = el.find("TargetGroups")
    if child_target_groups is not None:
        import aws_sdk_rds.types.target_group_list

        out["target_groups"] = aws_sdk_rds.types.target_group_list.deserialize_query(
            child_target_groups
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
