"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeUsersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.user_list


class DescribeUsersResult(TypedDict, closed=True):
    users: NotRequired["aws_sdk_elasticache.types.user_list.UserList"]
    """<p>A list of users.</p>"""
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords. ></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeUsersResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "users" in value:
        import aws_sdk_elasticache.types.user_list

        aws_sdk_elasticache.types.user_list.serialize_query(
            value["users"], pairs, f"{prefix}.Users"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeUsersResult:
    out: DescribeUsersResult = {}  # type: ignore[typeddict-item]
    child_users = el.find("Users")
    if child_users is not None:
        import aws_sdk_elasticache.types.user_list

        out["users"] = aws_sdk_elasticache.types.user_list.deserialize_query(
            child_users
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
