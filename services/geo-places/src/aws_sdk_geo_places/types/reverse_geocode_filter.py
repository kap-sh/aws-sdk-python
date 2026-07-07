"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.reverse_geocode_filter_place_type_list


class ReverseGeocodeFilter(TypedDict, closed=True):
    include_place_types: NotRequired[
        "aws_sdk_geo_places.types.reverse_geocode_filter_place_type_list.ReverseGeocodeFilterPlaceTypeList"
    ]
    r"""<p> The included place types. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>Street</code> and <code>PointAddress</code> values. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeFilter) -> dict:
    out: dict = {}
    if "include_place_types" in value:
        import aws_sdk_geo_places.types.reverse_geocode_filter_place_type_list

        out["IncludePlaceTypes"] = (
            aws_sdk_geo_places.types.reverse_geocode_filter_place_type_list.serialize_json(
                value["include_place_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReverseGeocodeFilter:
    out: ReverseGeocodeFilter = {}  # type: ignore[typeddict-item]
    if "IncludePlaceTypes" in data:
        import aws_sdk_geo_places.types.reverse_geocode_filter_place_type_list

        out["include_place_types"] = (
            aws_sdk_geo_places.types.reverse_geocode_filter_place_type_list.deserialize_json(
                data["IncludePlaceTypes"]
            )
        )
    return out
