"""Generated from Smithy shape ``com.amazonaws.glue#PhysicalConnectionRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.security_group_id_list


class PhysicalConnectionRequirements(TypedDict, closed=True):
    subnet_id: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The subnet ID used by the connection.</p>"""
    security_group_id_list: NotRequired[
        "capo_glue.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The security group ID list used by the connection.</p>"""
    availability_zone: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The connection's Availability Zone.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhysicalConnectionRequirements) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "security_group_id_list" in value:
        import capo_glue.types.security_group_id_list

        out["SecurityGroupIdList"] = (
            capo_glue.types.security_group_id_list.serialize_aws_json_1_1(
                value["security_group_id_list"]
            )
        )
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PhysicalConnectionRequirements:
    out: PhysicalConnectionRequirements = {}  # type: ignore[typeddict-item]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "SecurityGroupIdList" in data:
        import capo_glue.types.security_group_id_list

        out["security_group_id_list"] = (
            capo_glue.types.security_group_id_list.deserialize_aws_json_1_1(
                data["SecurityGroupIdList"]
            )
        )
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    return out
