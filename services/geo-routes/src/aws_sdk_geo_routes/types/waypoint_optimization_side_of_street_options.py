"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationSideOfStreetOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position
    import aws_sdk_geo_routes.types.side_of_street_matching_strategy


class WaypointOptimizationSideOfStreetOptions(TypedDict):
    position: "aws_sdk_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    use_with: NotRequired[
        "aws_sdk_geo_routes.types.side_of_street_matching_strategy.SideOfStreetMatchingStrategy"
    ]
    """<p>Strategy that defines when the side of street position should be used. AnyStreet will always use the provided position.</p> <p>Default value: <code>DividedStreetOnly</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationSideOfStreetOptions) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.position

    out["Position"] = aws_sdk_geo_routes.types.position.serialize_json(
        value["position"]
    )
    if "use_with" in value:
        import aws_sdk_geo_routes.types.side_of_street_matching_strategy

        out["UseWith"] = (
            aws_sdk_geo_routes.types.side_of_street_matching_strategy.serialize_json(
                value["use_with"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationSideOfStreetOptions:
    out: WaypointOptimizationSideOfStreetOptions = {}  # type: ignore[typeddict-item]
    if "Position" in data:
        import aws_sdk_geo_routes.types.position

        out["position"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError(
            "WaypointOptimizationSideOfStreetOptions.position required"
        )
    if "UseWith" in data:
        import aws_sdk_geo_routes.types.side_of_street_matching_strategy

        out["use_with"] = (
            aws_sdk_geo_routes.types.side_of_street_matching_strategy.deserialize_json(
                data["UseWith"]
            )
        )
    return out
