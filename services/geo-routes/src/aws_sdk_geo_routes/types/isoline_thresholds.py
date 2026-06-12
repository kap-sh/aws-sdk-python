"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineThresholds``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_threshold_list
    import aws_sdk_geo_routes.types.time_threshold_list


class IsolineThresholds(TypedDict):
    distance: NotRequired[
        "aws_sdk_geo_routes.types.distance_threshold_list.DistanceThresholdList"
    ]
    """<p>List of travel distances in meters. For example, [1000, 2000, 5000] would calculate areas reachable within 1, 2, and 5 kilometers.</p>"""
    time: NotRequired["aws_sdk_geo_routes.types.time_threshold_list.TimeThresholdList"]
    """<p>List of travel times in seconds. For example, [300, 600, 900] would calculate areas reachable within 5, 10, and 15 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineThresholds) -> dict:
    out: dict = {}
    if "distance" in value:
        import aws_sdk_geo_routes.types.distance_threshold_list

        out["Distance"] = (
            aws_sdk_geo_routes.types.distance_threshold_list.serialize_json(
                value["distance"]
            )
        )
    if "time" in value:
        import aws_sdk_geo_routes.types.time_threshold_list

        out["Time"] = aws_sdk_geo_routes.types.time_threshold_list.serialize_json(
            value["time"]
        )
    return out


def deserialize_json(data: dict) -> IsolineThresholds:
    out: IsolineThresholds = {}  # type: ignore[typeddict-item]
    if "Distance" in data:
        import aws_sdk_geo_routes.types.distance_threshold_list

        out["distance"] = (
            aws_sdk_geo_routes.types.distance_threshold_list.deserialize_json(
                data["Distance"]
            )
        )
    if "Time" in data:
        import aws_sdk_geo_routes.types.time_threshold_list

        out["time"] = aws_sdk_geo_routes.types.time_threshold_list.deserialize_json(
            data["Time"]
        )
    return out
