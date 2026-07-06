"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTravelModeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.road_snap_truck_options


class RoadSnapTravelModeOptions(TypedDict, closed=True):
    truck: NotRequired[
        "aws_sdk_geo_routes.types.road_snap_truck_options.RoadSnapTruckOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Truck</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapTravelModeOptions) -> dict:
    out: dict = {}
    if "truck" in value:
        import aws_sdk_geo_routes.types.road_snap_truck_options

        out["Truck"] = aws_sdk_geo_routes.types.road_snap_truck_options.serialize_json(
            value["truck"]
        )
    return out


def deserialize_json(data: dict) -> RoadSnapTravelModeOptions:
    out: RoadSnapTravelModeOptions = {}  # type: ignore[typeddict-item]
    if "Truck" in data:
        import aws_sdk_geo_routes.types.road_snap_truck_options

        out["truck"] = (
            aws_sdk_geo_routes.types.road_snap_truck_options.deserialize_json(
                data["Truck"]
            )
        )
    return out
