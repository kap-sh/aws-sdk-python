"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderVpcConfig``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_provider_security_group_ids
    import aws_sdk_lambda.types.capacity_provider_subnet_ids


class CapacityProviderVpcConfig(TypedDict):
    subnet_ids: (
        "aws_sdk_lambda.types.capacity_provider_subnet_ids.CapacityProviderSubnetIds"
    )
    """<p>A list of subnet IDs where the capacity provider launches compute instances.</p>"""
    security_group_ids: "aws_sdk_lambda.types.capacity_provider_security_group_ids.CapacityProviderSecurityGroupIds"
    """<p>A list of security group IDs that control network access for compute instances managed by the capacity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderVpcConfig) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.capacity_provider_subnet_ids

    out["SubnetIds"] = aws_sdk_lambda.types.capacity_provider_subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    import aws_sdk_lambda.types.capacity_provider_security_group_ids

    out["SecurityGroupIds"] = (
        aws_sdk_lambda.types.capacity_provider_security_group_ids.serialize_json(
            value["security_group_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> CapacityProviderVpcConfig:
    out: CapacityProviderVpcConfig = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import aws_sdk_lambda.types.capacity_provider_subnet_ids

        out["subnet_ids"] = (
            aws_sdk_lambda.types.capacity_provider_subnet_ids.deserialize_json(
                data["SubnetIds"]
            )
        )
    else:
        raise DeserializationError("CapacityProviderVpcConfig.subnet_ids required")
    if "SecurityGroupIds" in data:
        import aws_sdk_lambda.types.capacity_provider_security_group_ids

        out["security_group_ids"] = (
            aws_sdk_lambda.types.capacity_provider_security_group_ids.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "CapacityProviderVpcConfig.security_group_ids required"
        )
    return out
