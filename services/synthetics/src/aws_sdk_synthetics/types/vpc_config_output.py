"""Generated from Smithy shape ``com.amazonaws.synthetics#VpcConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.nullable_boolean
    import aws_sdk_synthetics.types.security_group_ids
    import aws_sdk_synthetics.types.subnet_ids
    import aws_sdk_synthetics.types.vpc_id


class VpcConfigOutput(TypedDict, closed=True):
    vpc_id: NotRequired["aws_sdk_synthetics.types.vpc_id.VpcId"]
    """<p>The IDs of the VPC where this canary is to run.</p>"""
    subnet_ids: NotRequired["aws_sdk_synthetics.types.subnet_ids.SubnetIds"]
    """<p>The IDs of the subnets where this canary is to run.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_synthetics.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The IDs of the security groups for this canary.</p>"""
    ipv6_allowed_for_dual_stack: NotRequired[
        "aws_sdk_synthetics.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether this canary allows outbound IPv6 traffic if it is connected to dual-stack subnets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfigOutput) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import aws_sdk_synthetics.types.subnet_ids

        out["SubnetIds"] = aws_sdk_synthetics.types.subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import aws_sdk_synthetics.types.security_group_ids

        out["SecurityGroupIds"] = (
            aws_sdk_synthetics.types.security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    if "ipv6_allowed_for_dual_stack" in value:
        out["Ipv6AllowedForDualStack"] = value["ipv6_allowed_for_dual_stack"]
    return out


def deserialize_json(data: dict) -> VpcConfigOutput:
    out: VpcConfigOutput = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetIds" in data:
        import aws_sdk_synthetics.types.subnet_ids

        out["subnet_ids"] = aws_sdk_synthetics.types.subnet_ids.deserialize_json(
            data["SubnetIds"]
        )
    if "SecurityGroupIds" in data:
        import aws_sdk_synthetics.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_synthetics.types.security_group_ids.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    if "Ipv6AllowedForDualStack" in data:
        out["ipv6_allowed_for_dual_stack"] = data["Ipv6AllowedForDualStack"]
    return out
