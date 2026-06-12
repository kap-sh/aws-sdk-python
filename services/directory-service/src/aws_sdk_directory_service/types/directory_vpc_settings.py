"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryVpcSettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.subnet_ids
    import aws_sdk_directory_service.types.vpc_id


class DirectoryVpcSettings(TypedDict):
    vpc_id: "aws_sdk_directory_service.types.vpc_id.VpcId"
    """<p>The identifier of the VPC in which to create the directory.</p>"""
    subnet_ids: "aws_sdk_directory_service.types.subnet_ids.SubnetIds"
    """<p>The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. Directory Service creates a directory server and a DNS server in each of these subnets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryVpcSettings) -> dict:
    out: dict = {}
    out["VpcId"] = value["vpc_id"]
    import aws_sdk_directory_service.types.subnet_ids

    out["SubnetIds"] = (
        aws_sdk_directory_service.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryVpcSettings:
    out: DirectoryVpcSettings = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    else:
        raise DeserializationError("DirectoryVpcSettings.vpc_id required")
    if "SubnetIds" in data:
        import aws_sdk_directory_service.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_directory_service.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        raise DeserializationError("DirectoryVpcSettings.subnet_ids required")
    return out
