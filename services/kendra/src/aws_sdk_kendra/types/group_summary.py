"""Generated from Smithy shape ``com.amazonaws.kendra#GroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.group_id
    import aws_sdk_kendra.types.principal_ordering_id


class GroupSummary(TypedDict, closed=True):
    group_id: NotRequired["aws_sdk_kendra.types.group_id.GroupId"]
    """<p>The identifier of the group you want group summary information on.</p>"""
    ordering_id: NotRequired[
        "aws_sdk_kendra.types.principal_ordering_id.PrincipalOrderingId"
    ]
    """<p>The timestamp identifier used for the latest <code>PUT</code> or <code>DELETE</code> action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupSummary) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "ordering_id" in value:
        out["OrderingId"] = value["ordering_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupSummary:
    out: GroupSummary = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    if "OrderingId" in data:
        out["ordering_id"] = data["OrderingId"]
    return out
