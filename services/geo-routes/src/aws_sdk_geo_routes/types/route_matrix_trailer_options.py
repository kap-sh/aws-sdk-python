"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixTrailerOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.sensitive_integer


class RouteMatrixTrailerOptions(TypedDict):
    trailer_count: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Number of trailers attached to the vehicle.</p> <p>Default value: <code>0</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixTrailerOptions) -> dict:
    out: dict = {}
    if "trailer_count" in value:
        out["TrailerCount"] = value["trailer_count"]
    return out


def deserialize_json(data: dict) -> RouteMatrixTrailerOptions:
    out: RouteMatrixTrailerOptions = {}  # type: ignore[typeddict-item]
    if "TrailerCount" in data:
        out["trailer_count"] = data["TrailerCount"]
    return out
