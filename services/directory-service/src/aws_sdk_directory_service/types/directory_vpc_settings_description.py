"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryVpcSettingsDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.availability_zones
    import aws_sdk_directory_service.types.security_group_id
    import aws_sdk_directory_service.types.subnet_ids
    import aws_sdk_directory_service.types.vpc_id


class DirectoryVpcSettingsDescription(TypedDict):
    vpc_id: NotRequired["aws_sdk_directory_service.types.vpc_id.VpcId"]
    """<p>The identifier of the VPC that the directory is in.</p>"""
    subnet_ids: NotRequired["aws_sdk_directory_service.types.subnet_ids.SubnetIds"]
    """<p>The identifiers of the subnets for the directory servers.</p>"""
    security_group_id: NotRequired[
        "aws_sdk_directory_service.types.security_group_id.SecurityGroupId"
    ]
    """<p>The domain controller security group identifier for the directory.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_directory_service.types.availability_zones.AvailabilityZones"
    ]
    """<p>The list of Availability Zones that the directory is in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryVpcSettingsDescription) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import aws_sdk_directory_service.types.subnet_ids

        out["SubnetIds"] = (
            aws_sdk_directory_service.types.subnet_ids.serialize_aws_json_1_1(
                value["subnet_ids"]
            )
        )
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    if "availability_zones" in value:
        import aws_sdk_directory_service.types.availability_zones

        out["AvailabilityZones"] = (
            aws_sdk_directory_service.types.availability_zones.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryVpcSettingsDescription:
    out: DirectoryVpcSettingsDescription = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetIds" in data:
        import aws_sdk_directory_service.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_directory_service.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    if "SecurityGroupId" in data:
        out["security_group_id"] = data["SecurityGroupId"]
    if "AvailabilityZones" in data:
        import aws_sdk_directory_service.types.availability_zones

        out["availability_zones"] = (
            aws_sdk_directory_service.types.availability_zones.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    return out
