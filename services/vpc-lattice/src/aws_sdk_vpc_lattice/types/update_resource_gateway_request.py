"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateResourceGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_gateway_identifier
    import aws_sdk_vpc_lattice.types.security_group_list


class UpdateResourceGatewayRequest(TypedDict, closed=True):
    resource_gateway_identifier: "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
    """<p>The ID or ARN of the resource gateway.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups associated with the resource gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceGatewayRequest) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import aws_sdk_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            aws_sdk_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateResourceGatewayRequest:
    out: UpdateResourceGatewayRequest = {}  # type: ignore[typeddict-item]
    if "securityGroupIds" in data:
        import aws_sdk_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            aws_sdk_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out
