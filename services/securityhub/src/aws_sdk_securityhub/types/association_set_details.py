"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociationSetDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.association_state_details
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AssociationSetDetails(TypedDict):
    association_state: NotRequired[
        "aws_sdk_securityhub.types.association_state_details.AssociationStateDetails"
    ]
    """<p> The state of the association between a route table and a subnet or gateway. </p>"""
    gateway_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the internet gateway or virtual private gateway. </p>"""
    main: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether this is the main route table. </p>"""
    route_table_association_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the association. </p>"""
    route_table_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the route table. </p>"""
    subnet_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the subnet. A subnet ID is not returned for an implicit association. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociationSetDetails) -> dict:
    out: dict = {}
    if "association_state" in value:
        import aws_sdk_securityhub.types.association_state_details

        out["AssociationState"] = (
            aws_sdk_securityhub.types.association_state_details.serialize_json(
                value["association_state"]
            )
        )
    if "gateway_id" in value:
        out["GatewayId"] = value["gateway_id"]
    if "main" in value:
        out["Main"] = value["main"]
    if "route_table_association_id" in value:
        out["RouteTableAssociationId"] = value["route_table_association_id"]
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    return out


def deserialize_json(data: dict) -> AssociationSetDetails:
    out: AssociationSetDetails = {}  # type: ignore[typeddict-item]
    if "AssociationState" in data:
        import aws_sdk_securityhub.types.association_state_details

        out["association_state"] = (
            aws_sdk_securityhub.types.association_state_details.deserialize_json(
                data["AssociationState"]
            )
        )
    if "GatewayId" in data:
        out["gateway_id"] = data["GatewayId"]
    if "Main" in data:
        out["main"] = data["Main"]
    if "RouteTableAssociationId" in data:
        out["route_table_association_id"] = data["RouteTableAssociationId"]
    if "RouteTableId" in data:
        out["route_table_id"] = data["RouteTableId"]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    return out
