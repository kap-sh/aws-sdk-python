"""Generated from Smithy shape ``com.amazonaws.outposts#RackSpecificationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.ec2_capacity_list_definition
    import capo_outposts.types.nullable_float
    import capo_outposts.types.quote_rack_use_type
    import capo_outposts.types.rack_id
    import capo_outposts.types.rack_unit_height


class RackSpecificationDetails(TypedDict, closed=True):
    rack_id: NotRequired["capo_outposts.types.rack_id.RackId"]
    """<p>The ID of the rack.</p>"""
    rack_use: NotRequired["capo_outposts.types.quote_rack_use_type.QuoteRackUseType"]
    """<p>The use of the rack. Valid values are <code>COMPUTE</code> and <code>NETWORKING</code>.</p>"""
    rack_power_draw_kva: NotRequired["capo_outposts.types.nullable_float.NullableFloat"]
    """<p>The maximum power draw of the rack in kVA.</p>"""
    rack_weight_lbs: NotRequired["capo_outposts.types.nullable_float.NullableFloat"]
    """<p>The weight of the rack in pounds.</p>"""
    rack_height_inches: NotRequired["capo_outposts.types.nullable_float.NullableFloat"]
    """<p>The height of the rack in inches.</p>"""
    rack_width_inches: NotRequired["capo_outposts.types.nullable_float.NullableFloat"]
    """<p>The width of the rack in inches.</p>"""
    rack_depth_inches: NotRequired["capo_outposts.types.nullable_float.NullableFloat"]
    """<p>The depth of the rack in inches.</p>"""
    rack_unit_height: NotRequired["capo_outposts.types.rack_unit_height.RackUnitHeight"]
    """<p>The rack unit height.</p> <ul> <li> <p> <code>HEIGHT_42U</code> - 42 rack units.</p> </li> <li> <p> <code>HEIGHT_2U</code> - 2 rack units.</p> </li> <li> <p> <code>HEIGHT_1U</code> - 1 rack unit.</p> </li> </ul>"""
    ec2_capacities: NotRequired[
        "capo_outposts.types.ec2_capacity_list_definition.EC2CapacityListDefinition"
    ]
    """<p>The Amazon EC2 capacities for the rack.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RackSpecificationDetails) -> dict:
    out: dict = {}
    if "rack_id" in value:
        out["RackId"] = value["rack_id"]
    if "rack_use" in value:
        import capo_outposts.types.quote_rack_use_type

        out["RackUse"] = capo_outposts.types.quote_rack_use_type.serialize_json(
            value["rack_use"]
        )
    if "rack_power_draw_kva" in value:
        out["RackPowerDrawKva"] = value["rack_power_draw_kva"]
    if "rack_weight_lbs" in value:
        out["RackWeightLbs"] = value["rack_weight_lbs"]
    if "rack_height_inches" in value:
        out["RackHeightInches"] = value["rack_height_inches"]
    if "rack_width_inches" in value:
        out["RackWidthInches"] = value["rack_width_inches"]
    if "rack_depth_inches" in value:
        out["RackDepthInches"] = value["rack_depth_inches"]
    if "rack_unit_height" in value:
        import capo_outposts.types.rack_unit_height

        out["RackUnitHeight"] = capo_outposts.types.rack_unit_height.serialize_json(
            value["rack_unit_height"]
        )
    if "ec2_capacities" in value:
        import capo_outposts.types.ec2_capacity_list_definition

        out["EC2Capacities"] = (
            capo_outposts.types.ec2_capacity_list_definition.serialize_json(
                value["ec2_capacities"]
            )
        )
    return out


def deserialize_json(data: dict) -> RackSpecificationDetails:
    out: RackSpecificationDetails = {}  # type: ignore[typeddict-item]
    if "RackId" in data:
        out["rack_id"] = data["RackId"]
    if "RackUse" in data:
        import capo_outposts.types.quote_rack_use_type

        out["rack_use"] = capo_outposts.types.quote_rack_use_type.deserialize_json(
            data["RackUse"]
        )
    if "RackPowerDrawKva" in data:
        out["rack_power_draw_kva"] = data["RackPowerDrawKva"]
    if "RackWeightLbs" in data:
        out["rack_weight_lbs"] = data["RackWeightLbs"]
    if "RackHeightInches" in data:
        out["rack_height_inches"] = data["RackHeightInches"]
    if "RackWidthInches" in data:
        out["rack_width_inches"] = data["RackWidthInches"]
    if "RackDepthInches" in data:
        out["rack_depth_inches"] = data["RackDepthInches"]
    if "RackUnitHeight" in data:
        import capo_outposts.types.rack_unit_height

        out["rack_unit_height"] = capo_outposts.types.rack_unit_height.deserialize_json(
            data["RackUnitHeight"]
        )
    if "EC2Capacities" in data:
        import capo_outposts.types.ec2_capacity_list_definition

        out["ec2_capacities"] = (
            capo_outposts.types.ec2_capacity_list_definition.deserialize_json(
                data["EC2Capacities"]
            )
        )
    return out
