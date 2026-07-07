"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateIpGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ip_group_id


class CreateIpGroupResult(TypedDict, closed=True):
    group_id: NotRequired["aws_sdk_workspaces.types.ip_group_id.IpGroupId"]
    """<p>The identifier of the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIpGroupResult) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIpGroupResult:
    out: CreateIpGroupResult = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    return out
