"""Generated from Smithy shape ``com.amazonaws.iam#GetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.boolean_type
    import aws_sdk_iam.types.group
    import aws_sdk_iam.types.response_marker_type
    import aws_sdk_iam.types.user_list_type


class GetGroupResponse(TypedDict, closed=True):
    group: "aws_sdk_iam.types.group.Group"
    """<p>A structure that contains details about the group.</p>"""
    users: "aws_sdk_iam.types.user_list_type.userListType"
    """<p>A list of users in the group.</p>"""
    is_truncated: "aws_sdk_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. Note that IAM might return fewer than the <code>MaxItems</code> number of results even when there are more results available. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["aws_sdk_iam.types.response_marker_type.responseMarkerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetGroupResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.group

    aws_sdk_iam.types.group.serialize_query(value["group"], pairs, f"{prefix}.Group")
    import aws_sdk_iam.types.user_list_type

    aws_sdk_iam.types.user_list_type.serialize_query(
        value["users"], pairs, f"{prefix}.Users"
    )
    pairs.append(
        (
            f"{prefix}.IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> GetGroupResponse:
    out: GetGroupResponse = {}  # type: ignore[typeddict-item]
    child_group = el.find("Group")
    if child_group is not None:
        import aws_sdk_iam.types.group

        out["group"] = aws_sdk_iam.types.group.deserialize_query(child_group)
    else:
        raise DeserializationError("GetGroupResponse.group required")
    child_users = el.find("Users")
    if child_users is not None:
        import aws_sdk_iam.types.user_list_type

        out["users"] = aws_sdk_iam.types.user_list_type.deserialize_query(child_users)
    else:
        raise DeserializationError("GetGroupResponse.users required")
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
