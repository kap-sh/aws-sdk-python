"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWeightConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_weight_constraint_type
    import aws_sdk_geo_routes.types.weight_kilograms


class RouteWeightConstraint(TypedDict, closed=True):
    type: "aws_sdk_geo_routes.types.route_weight_constraint_type.RouteWeightConstraintType"
    """<p>The type of constraint.</p>"""
    value: "aws_sdk_geo_routes.types.weight_kilograms.WeightKilograms"
    """<p>The constraint value.</p> <p> <b>Unit</b>: <code>kilograms</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteWeightConstraint) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_weight_constraint_type

    out["Type"] = aws_sdk_geo_routes.types.route_weight_constraint_type.serialize_json(
        value["type"]
    )
    out["Value"] = value.get("value", 0)
    return out


def deserialize_json(data: dict) -> RouteWeightConstraint:
    out: RouteWeightConstraint = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_geo_routes.types.route_weight_constraint_type

        out["type"] = (
            aws_sdk_geo_routes.types.route_weight_constraint_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteWeightConstraint.type required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    return out
