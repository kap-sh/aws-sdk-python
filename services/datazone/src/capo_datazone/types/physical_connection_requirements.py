"""Generated from Smithy shape ``com.amazonaws.datazone#PhysicalConnectionRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.security_group_id_list
    import capo_datazone.types.subnet_id
    import capo_datazone.types.subnet_id_list


class PhysicalConnectionRequirements(TypedDict, closed=True):
    subnet_id: NotRequired["capo_datazone.types.subnet_id.SubnetId"]
    """<p>The subnet ID of the physical connection requirements of a connection. </p>"""
    subnet_id_list: NotRequired["capo_datazone.types.subnet_id_list.SubnetIdList"]
    """<p>The subnet ID list of the physical connection requirements of a connection. </p>"""
    security_group_id_list: NotRequired[
        "capo_datazone.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The group ID list of the physical connection requirements of a connection. </p>"""
    availability_zone: NotRequired["str"]
    """<p>The availability zone of the physical connection requirements of a connection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalConnectionRequirements) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "subnet_id_list" in value:
        import capo_datazone.types.subnet_id_list

        out["subnetIdList"] = capo_datazone.types.subnet_id_list.serialize_json(
            value["subnet_id_list"]
        )
    if "security_group_id_list" in value:
        import capo_datazone.types.security_group_id_list

        out["securityGroupIdList"] = (
            capo_datazone.types.security_group_id_list.serialize_json(
                value["security_group_id_list"]
            )
        )
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    return out


def deserialize_json(data: dict) -> PhysicalConnectionRequirements:
    out: PhysicalConnectionRequirements = {}  # type: ignore[typeddict-item]
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    if "subnetIdList" in data:
        import capo_datazone.types.subnet_id_list

        out["subnet_id_list"] = capo_datazone.types.subnet_id_list.deserialize_json(
            data["subnetIdList"]
        )
    if "securityGroupIdList" in data:
        import capo_datazone.types.security_group_id_list

        out["security_group_id_list"] = (
            capo_datazone.types.security_group_id_list.deserialize_json(
                data["securityGroupIdList"]
            )
        )
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    return out
