"""Generated from Smithy shape ``com.amazonaws.outposts#ServerSpecificationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.ec2_capacity_list_definition
    import capo_outposts.types.nullable_float
    import capo_outposts.types.rack_unit_height


class ServerSpecificationDetails(TypedDict, closed=True):
    server_power_draw_kva: NotRequired[
        "capo_outposts.types.nullable_float.NullableFloat"
    ]
    """<p>The maximum power draw of the server in kVA.</p>"""
    server_weight_lbs: NotRequired["capo_outposts.types.nullable_float.NullableFloat"]
    """<p>The weight of the server in pounds.</p>"""
    server_height_inches: NotRequired[
        "capo_outposts.types.nullable_float.NullableFloat"
    ]
    """<p>The height of the server in inches.</p>"""
    server_width_inches: NotRequired["capo_outposts.types.nullable_float.NullableFloat"]
    """<p>The width of the server in inches.</p>"""
    server_depth_inches: NotRequired["capo_outposts.types.nullable_float.NullableFloat"]
    """<p>The depth of the server in inches.</p>"""
    rack_unit_height: NotRequired["capo_outposts.types.rack_unit_height.RackUnitHeight"]
    """<p>The rack unit height of the server.</p> <ul> <li> <p> <code>HEIGHT_2U</code> - 2 rack units.</p> </li> <li> <p> <code>HEIGHT_1U</code> - 1 rack unit.</p> </li> </ul>"""
    ec2_capacities: NotRequired[
        "capo_outposts.types.ec2_capacity_list_definition.EC2CapacityListDefinition"
    ]
    """<p>The Amazon EC2 capacities for the server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerSpecificationDetails) -> dict:
    out: dict = {}
    if "server_power_draw_kva" in value:
        out["ServerPowerDrawKva"] = value["server_power_draw_kva"]
    if "server_weight_lbs" in value:
        out["ServerWeightLbs"] = value["server_weight_lbs"]
    if "server_height_inches" in value:
        out["ServerHeightInches"] = value["server_height_inches"]
    if "server_width_inches" in value:
        out["ServerWidthInches"] = value["server_width_inches"]
    if "server_depth_inches" in value:
        out["ServerDepthInches"] = value["server_depth_inches"]
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


def deserialize_json(data: dict) -> ServerSpecificationDetails:
    out: ServerSpecificationDetails = {}  # type: ignore[typeddict-item]
    if "ServerPowerDrawKva" in data:
        out["server_power_draw_kva"] = data["ServerPowerDrawKva"]
    if "ServerWeightLbs" in data:
        out["server_weight_lbs"] = data["ServerWeightLbs"]
    if "ServerHeightInches" in data:
        out["server_height_inches"] = data["ServerHeightInches"]
    if "ServerWidthInches" in data:
        out["server_width_inches"] = data["ServerWidthInches"]
    if "ServerDepthInches" in data:
        out["server_depth_inches"] = data["ServerDepthInches"]
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
