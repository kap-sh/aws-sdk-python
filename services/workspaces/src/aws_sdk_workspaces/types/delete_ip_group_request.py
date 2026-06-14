"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteIpGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ip_group_id


class DeleteIpGroupRequest(TypedDict):
    group_id: "aws_sdk_workspaces.types.ip_group_id.IpGroupId"
    """<p>The identifier of the IP access control group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIpGroupRequest) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIpGroupRequest:
    out: DeleteIpGroupRequest = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("DeleteIpGroupRequest.group_id required")
    return out
