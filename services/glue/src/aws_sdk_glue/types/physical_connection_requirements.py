"""Generated from Smithy shape ``com.amazonaws.glue#PhysicalConnectionRequirements``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.security_group_id_list


class PhysicalConnectionRequirements(TypedDict):
    subnet_id: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The subnet ID used by the connection.</p>"""
    security_group_id_list: NotRequired[
        "aws_sdk_glue.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The security group ID list used by the connection.</p>"""
    availability_zone: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The connection's Availability Zone.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhysicalConnectionRequirements) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "security_group_id_list" in value:
        import aws_sdk_glue.types.security_group_id_list

        out["SecurityGroupIdList"] = (
            aws_sdk_glue.types.security_group_id_list.serialize_aws_json_1_1(
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
        import aws_sdk_glue.types.security_group_id_list

        out["security_group_id_list"] = (
            aws_sdk_glue.types.security_group_id_list.deserialize_aws_json_1_1(
                data["SecurityGroupIdList"]
            )
        )
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    return out
