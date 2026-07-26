"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2RouteTableDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.association_set_list
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.propagating_vgw_set_list
    import capo_securityhub.types.route_set_list


class AwsEc2RouteTableDetails(TypedDict, closed=True):
    association_set: NotRequired[
        "capo_securityhub.types.association_set_list.AssociationSetList"
    ]
    """<p> The associations between a route table and one or more subnets or a gateway. </p>"""
    owner_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the Amazon Web Services account that owns the route table. </p>"""
    propagating_vgw_set: NotRequired[
        "capo_securityhub.types.propagating_vgw_set_list.PropagatingVgwSetList"
    ]
    """<p> Describes a virtual private gateway propagating route. </p>"""
    route_table_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the route table. </p>"""
    route_set: NotRequired["capo_securityhub.types.route_set_list.RouteSetList"]
    """<p> The routes in the route table. </p>"""
    vpc_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the virtual private cloud (VPC). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2RouteTableDetails) -> dict:
    out: dict = {}
    if "association_set" in value:
        import capo_securityhub.types.association_set_list

        out["AssociationSet"] = (
            capo_securityhub.types.association_set_list.serialize_json(
                value["association_set"]
            )
        )
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "propagating_vgw_set" in value:
        import capo_securityhub.types.propagating_vgw_set_list

        out["PropagatingVgwSet"] = (
            capo_securityhub.types.propagating_vgw_set_list.serialize_json(
                value["propagating_vgw_set"]
            )
        )
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "route_set" in value:
        import capo_securityhub.types.route_set_list

        out["RouteSet"] = capo_securityhub.types.route_set_list.serialize_json(
            value["route_set"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2RouteTableDetails:
    out: AwsEc2RouteTableDetails = {}  # type: ignore[typeddict-item]
    if "AssociationSet" in data:
        import capo_securityhub.types.association_set_list

        out["association_set"] = (
            capo_securityhub.types.association_set_list.deserialize_json(
                data["AssociationSet"]
            )
        )
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "PropagatingVgwSet" in data:
        import capo_securityhub.types.propagating_vgw_set_list

        out["propagating_vgw_set"] = (
            capo_securityhub.types.propagating_vgw_set_list.deserialize_json(
                data["PropagatingVgwSet"]
            )
        )
    if "RouteTableId" in data:
        out["route_table_id"] = data["RouteTableId"]
    if "RouteSet" in data:
        import capo_securityhub.types.route_set_list

        out["route_set"] = capo_securityhub.types.route_set_list.deserialize_json(
            data["RouteSet"]
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
