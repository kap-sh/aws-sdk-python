"""Generated from Smithy shape ``com.amazonaws.location#CalculateRouteMatrixSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.distance_unit


class CalculateRouteMatrixSummary(TypedDict):
    data_source: "str"
    """<p>The data provider of traffic and road network data used to calculate the routes. Indicates one of the available providers:</p> <ul> <li> <p> <code>Esri</code> </p> </li> <li> <p> <code>Grab</code> </p> </li> <li> <p> <code>Here</code> </p> </li> </ul> <p>For more information about data providers, see <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html\">Amazon Location Service data providers</a>.</p>"""
    route_count: "int"
    """<p>The count of cells in the route matrix. Equal to the number of <code>DeparturePositions</code> multiplied by the number of <code>DestinationPositions</code>.</p>"""
    error_count: "int"
    """<p>The count of error results in the route matrix. If this number is 0, all routes were calculated successfully.</p>"""
    distance_unit: "aws_sdk_location.types.distance_unit.DistanceUnit"
    """<p>The unit of measurement for route distances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteMatrixSummary) -> dict:
    out: dict = {}
    out["DataSource"] = value["data_source"]
    out["RouteCount"] = value["route_count"]
    out["ErrorCount"] = value["error_count"]
    out["DistanceUnit"] = value["distance_unit"]
    return out


def deserialize_json(data: dict) -> CalculateRouteMatrixSummary:
    out: CalculateRouteMatrixSummary = {}  # type: ignore[typeddict-item]
    if "DataSource" in data:
        out["data_source"] = data["DataSource"]
    else:
        raise DeserializationError("CalculateRouteMatrixSummary.data_source required")
    if "RouteCount" in data:
        out["route_count"] = data["RouteCount"]
    else:
        raise DeserializationError("CalculateRouteMatrixSummary.route_count required")
    if "ErrorCount" in data:
        out["error_count"] = data["ErrorCount"]
    else:
        raise DeserializationError("CalculateRouteMatrixSummary.error_count required")
    if "DistanceUnit" in data:
        out["distance_unit"] = data["DistanceUnit"]
    else:
        raise DeserializationError("CalculateRouteMatrixSummary.distance_unit required")
    return out
