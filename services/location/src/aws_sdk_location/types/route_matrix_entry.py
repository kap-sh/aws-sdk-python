"""Generated from Smithy shape ``com.amazonaws.location#RouteMatrixEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_location.types.route_matrix_entry_error
    import aws_sdk_location.types.sensitive_double


class RouteMatrixEntry(TypedDict):
    distance: NotRequired["aws_sdk_location.types.sensitive_double.SensitiveDouble"]
    """<p>The total distance of travel for the route.</p>"""
    duration_seconds: NotRequired[
        "aws_sdk_location.types.sensitive_double.SensitiveDouble"
    ]
    """<p>The expected duration of travel for the route.</p>"""
    error: NotRequired[
        "aws_sdk_location.types.route_matrix_entry_error.RouteMatrixEntryError"
    ]
    """<p>An error corresponding to the calculation of a route between the <code>DeparturePosition</code> and <code>DestinationPosition</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixEntry) -> dict:
    out: dict = {}
    if "distance" in value:
        out["Distance"] = value["distance"]
    if "duration_seconds" in value:
        out["DurationSeconds"] = value["duration_seconds"]
    if "error" in value:
        import aws_sdk_location.types.route_matrix_entry_error

        out["Error"] = aws_sdk_location.types.route_matrix_entry_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixEntry:
    out: RouteMatrixEntry = {}  # type: ignore[typeddict-item]
    if "Distance" in data:
        out["distance"] = data["Distance"]
    if "DurationSeconds" in data:
        out["duration_seconds"] = data["DurationSeconds"]
    if "Error" in data:
        import aws_sdk_location.types.route_matrix_entry_error

        out["error"] = aws_sdk_location.types.route_matrix_entry_error.deserialize_json(
            data["Error"]
        )
    return out
