"""Generated from Smithy shape ``com.amazonaws.devicefarm#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.non_empty_string
    import aws_sdk_device_farm.types.vpc_security_group_ids
    import aws_sdk_device_farm.types.vpc_subnet_ids


class VpcConfig(TypedDict, closed=True):
    security_group_ids: (
        "aws_sdk_device_farm.types.vpc_security_group_ids.VpcSecurityGroupIds"
    )
    """<p>An array of one or more security groups IDs in your Amazon VPC.</p>"""
    subnet_ids: "aws_sdk_device_farm.types.vpc_subnet_ids.VpcSubnetIds"
    """<p>An array of one or more subnet IDs in your Amazon VPC.</p>"""
    vpc_id: "aws_sdk_device_farm.types.non_empty_string.NonEmptyString"
    """<p>The ID of the Amazon VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfig) -> dict:
    out: dict = {}
    import aws_sdk_device_farm.types.vpc_security_group_ids

    out["securityGroupIds"] = (
        aws_sdk_device_farm.types.vpc_security_group_ids.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    )
    import aws_sdk_device_farm.types.vpc_subnet_ids

    out["subnetIds"] = aws_sdk_device_farm.types.vpc_subnet_ids.serialize_aws_json_1_1(
        value["subnet_ids"]
    )
    out["vpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if "securityGroupIds" in data:
        import aws_sdk_device_farm.types.vpc_security_group_ids

        out["security_group_ids"] = (
            aws_sdk_device_farm.types.vpc_security_group_ids.deserialize_aws_json_1_1(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfig.security_group_ids required")
    if "subnetIds" in data:
        import aws_sdk_device_farm.types.vpc_subnet_ids

        out["subnet_ids"] = (
            aws_sdk_device_farm.types.vpc_subnet_ids.deserialize_aws_json_1_1(
                data["subnetIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfig.subnet_ids required")
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("VpcConfig.vpc_id required")
    return out
