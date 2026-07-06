"""Generated from Smithy shape ``com.amazonaws.bedrock#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.security_group_ids
    import aws_sdk_bedrock.types.subnet_ids


class VpcConfig(TypedDict, closed=True):
    subnet_ids: "aws_sdk_bedrock.types.subnet_ids.SubnetIds"
    """<p>An array of IDs for each subnet in the VPC to use.</p>"""
    security_group_ids: "aws_sdk_bedrock.types.security_group_ids.SecurityGroupIds"
    """<p>An array of IDs for each security group in the VPC to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfig) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.subnet_ids

    out["subnetIds"] = aws_sdk_bedrock.types.subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    import aws_sdk_bedrock.types.security_group_ids

    out["securityGroupIds"] = aws_sdk_bedrock.types.security_group_ids.serialize_json(
        value["security_group_ids"]
    )
    return out


def deserialize_json(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import aws_sdk_bedrock.types.subnet_ids

        out["subnet_ids"] = aws_sdk_bedrock.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("VpcConfig.subnet_ids required")
    if "securityGroupIds" in data:
        import aws_sdk_bedrock.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_bedrock.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfig.security_group_ids required")
    return out
