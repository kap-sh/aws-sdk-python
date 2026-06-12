"""Generated from Smithy shape ``com.amazonaws.synthetics#VpcConfigInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.nullable_boolean
    import aws_sdk_synthetics.types.security_group_ids
    import aws_sdk_synthetics.types.subnet_ids


class VpcConfigInput(TypedDict):
    subnet_ids: NotRequired["aws_sdk_synthetics.types.subnet_ids.SubnetIds"]
    """<p>The IDs of the subnets where this canary is to run.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_synthetics.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The IDs of the security groups for this canary.</p>"""
    ipv6_allowed_for_dual_stack: NotRequired[
        "aws_sdk_synthetics.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Set this to <code>true</code> to allow outbound IPv6 traffic on VPC canaries that are connected to dual-stack subnets. The default is <code>false</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfigInput) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> VpcConfigInput:
    out: VpcConfigInput = {}  # type: ignore[typeddict-item]
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
