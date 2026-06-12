"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridVpcConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.non_empty_string
    import aws_sdk_device_farm.types.security_group_ids
    import aws_sdk_device_farm.types.subnet_ids


class TestGridVpcConfig(TypedDict):
    security_group_ids: "aws_sdk_device_farm.types.security_group_ids.SecurityGroupIds"
    """<p>A list of VPC security group IDs in your Amazon VPC.</p>"""
    subnet_ids: "aws_sdk_device_farm.types.subnet_ids.SubnetIds"
    """<p>A list of VPC subnet IDs in your Amazon VPC.</p>"""
    vpc_id: "aws_sdk_device_farm.types.non_empty_string.NonEmptyString"
    """<p>The ID of the Amazon VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridVpcConfig) -> dict:
    out: dict = {}
    import aws_sdk_device_farm.types.security_group_ids

    out["securityGroupIds"] = (
        aws_sdk_device_farm.types.security_group_ids.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    )
    import aws_sdk_device_farm.types.subnet_ids

    out["subnetIds"] = aws_sdk_device_farm.types.subnet_ids.serialize_aws_json_1_1(
        value["subnet_ids"]
    )
    out["vpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestGridVpcConfig:
    out: TestGridVpcConfig = {}  # type: ignore[typeddict-item]
    if "securityGroupIds" in data:
        import aws_sdk_device_farm.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_device_farm.types.security_group_ids.deserialize_aws_json_1_1(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError("TestGridVpcConfig.security_group_ids required")
    if "subnetIds" in data:
        import aws_sdk_device_farm.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_device_farm.types.subnet_ids.deserialize_aws_json_1_1(
                data["subnetIds"]
            )
        )
    else:
        raise DeserializationError("TestGridVpcConfig.subnet_ids required")
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("TestGridVpcConfig.vpc_id required")
    return out
