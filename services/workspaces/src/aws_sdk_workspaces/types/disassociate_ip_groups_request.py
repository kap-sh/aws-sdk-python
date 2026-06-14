"""Generated from Smithy shape ``com.amazonaws.workspaces#DisassociateIpGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.ip_group_id_list


class DisassociateIpGroupsRequest(TypedDict):
    directory_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    group_ids: "aws_sdk_workspaces.types.ip_group_id_list.IpGroupIdList"
    """<p>The identifiers of one or more IP access control groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateIpGroupsRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import aws_sdk_workspaces.types.ip_group_id_list

    out["GroupIds"] = aws_sdk_workspaces.types.ip_group_id_list.serialize_aws_json_1_1(
        value["group_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateIpGroupsRequest:
    out: DisassociateIpGroupsRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("DisassociateIpGroupsRequest.directory_id required")
    if "GroupIds" in data:
        import aws_sdk_workspaces.types.ip_group_id_list

        out["group_ids"] = (
            aws_sdk_workspaces.types.ip_group_id_list.deserialize_aws_json_1_1(
                data["GroupIds"]
            )
        )
    else:
        raise DeserializationError("DisassociateIpGroupsRequest.group_ids required")
    return out
