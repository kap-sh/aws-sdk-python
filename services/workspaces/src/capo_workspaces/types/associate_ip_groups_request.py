"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociateIpGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.ip_group_id_list


class AssociateIpGroupsRequest(TypedDict, closed=True):
    directory_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    group_ids: "capo_workspaces.types.ip_group_id_list.IpGroupIdList"
    """<p>The identifiers of one or more IP access control groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateIpGroupsRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_workspaces.types.ip_group_id_list

    out["GroupIds"] = capo_workspaces.types.ip_group_id_list.serialize_aws_json_1_1(
        value["group_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateIpGroupsRequest:
    out: AssociateIpGroupsRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("AssociateIpGroupsRequest.directory_id required")
    if "GroupIds" in data:
        import capo_workspaces.types.ip_group_id_list

        out["group_ids"] = (
            capo_workspaces.types.ip_group_id_list.deserialize_aws_json_1_1(
                data["GroupIds"]
            )
        )
    else:
        raise DeserializationError("AssociateIpGroupsRequest.group_ids required")
    return out
