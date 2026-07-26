"""Generated from Smithy shape ``com.amazonaws.lambda#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.nullable_boolean
    import capo_lambda.types.security_group_ids
    import capo_lambda.types.subnet_ids


class VpcConfig(TypedDict, closed=True):
    subnet_ids: NotRequired["capo_lambda.types.subnet_ids.SubnetIds"]
    """<p>A list of VPC subnet IDs.</p>"""
    security_group_ids: NotRequired[
        "capo_lambda.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of VPC security group IDs.</p>"""
    ipv6_allowed_for_dual_stack: NotRequired[
        "capo_lambda.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Allows outbound IPv6 traffic on VPC functions that are connected to dual-stack subnets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfig) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_lambda.types.subnet_ids

        out["SubnetIds"] = capo_lambda.types.subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_lambda.types.security_group_ids

        out["SecurityGroupIds"] = capo_lambda.types.security_group_ids.serialize_json(
            value["security_group_ids"]
        )
    if "ipv6_allowed_for_dual_stack" in value:
        out["Ipv6AllowedForDualStack"] = value["ipv6_allowed_for_dual_stack"]
    return out


def deserialize_json(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import capo_lambda.types.subnet_ids

        out["subnet_ids"] = capo_lambda.types.subnet_ids.deserialize_json(
            data["SubnetIds"]
        )
    if "SecurityGroupIds" in data:
        import capo_lambda.types.security_group_ids

        out["security_group_ids"] = (
            capo_lambda.types.security_group_ids.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    if "Ipv6AllowedForDualStack" in data:
        out["ipv6_allowed_for_dual_stack"] = data["Ipv6AllowedForDualStack"]
    return out
