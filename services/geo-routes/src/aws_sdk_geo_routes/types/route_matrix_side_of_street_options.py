"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixSideOfStreetOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position
    import aws_sdk_geo_routes.types.side_of_street_matching_strategy


class RouteMatrixSideOfStreetOptions(TypedDict, closed=True):
    position: "aws_sdk_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    use_with: NotRequired[
        "aws_sdk_geo_routes.types.side_of_street_matching_strategy.SideOfStreetMatchingStrategy"
    ]
    """<p>Strategy that defines when the side of street position should be used. AnyStreet will always use the provided position.</p> <p>Default value: <code>DividedStreetOnly</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixSideOfStreetOptions) -> dict:
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


def deserialize_json(data: dict) -> RouteMatrixSideOfStreetOptions:
    out: RouteMatrixSideOfStreetOptions = {}  # type: ignore[typeddict-item]
    if "Position" in data:
        import aws_sdk_geo_routes.types.position

        out["position"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteMatrixSideOfStreetOptions.position required")
    if "UseWith" in data:
        import aws_sdk_geo_routes.types.side_of_street_matching_strategy

        out["use_with"] = (
            aws_sdk_geo_routes.types.side_of_street_matching_strategy.deserialize_json(
                data["UseWith"]
            )
        )
    return out
