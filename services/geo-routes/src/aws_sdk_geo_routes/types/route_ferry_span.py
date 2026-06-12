"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerrySpan``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.country_code3
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.localized_string_list
    import aws_sdk_geo_routes.types.sensitive_string


class RouteFerrySpan(TypedDict):
    country: NotRequired["aws_sdk_geo_routes.types.country_code3.CountryCode3"]
    """<p>3 letter Country code corresponding to the Span.</p>"""
    distance: "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this span.</p>"""
    names: NotRequired[
        "aws_sdk_geo_routes.types.localized_string_list.LocalizedStringList"
    ]
    """<p>Names of the ferry span in available languages.</p>"""
    region: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>2-3 letter Region code corresponding to the Span. This is either a province or a state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerrySpan) -> dict:
    out: dict = {}
    if "country" in value:
        out["Country"] = value["country"]
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "names" in value:
        import aws_sdk_geo_routes.types.localized_string_list

        out["Names"] = aws_sdk_geo_routes.types.localized_string_list.serialize_json(
            value["names"]
        )
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> RouteFerrySpan:
    out: RouteFerrySpan = {}  # type: ignore[typeddict-item]
    if "Country" in data:
        out["country"] = data["Country"]
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "GeometryOffset" in data:
        out["geometry_offset"] = data["GeometryOffset"]
    if "Names" in data:
        import aws_sdk_geo_routes.types.localized_string_list

        out["names"] = aws_sdk_geo_routes.types.localized_string_list.deserialize_json(
            data["Names"]
        )
    if "Region" in data:
        out["region"] = data["Region"]
    return out
