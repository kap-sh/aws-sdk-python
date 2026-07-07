"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.autocomplete_filter_place_type_list
    import aws_sdk_geo_places.types.bounding_box
    import aws_sdk_geo_places.types.country_code_list
    import aws_sdk_geo_places.types.filter_circle


class AutocompleteFilter(TypedDict, closed=True):
    bounding_box: NotRequired["aws_sdk_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set 4 coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    circle: NotRequired["aws_sdk_geo_places.types.filter_circle.FilterCircle"]
    include_countries: NotRequired[
        "aws_sdk_geo_places.types.country_code_list.CountryCodeList"
    ]
    """<p> A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.</p>"""
    include_place_types: NotRequired[
        "aws_sdk_geo_places.types.autocomplete_filter_place_type_list.AutocompleteFilterPlaceTypeList"
    ]
    """<p>The included place types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteFilter) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import aws_sdk_geo_places.types.bounding_box

        out["BoundingBox"] = aws_sdk_geo_places.types.bounding_box.serialize_json(
            value["bounding_box"]
        )
    if "circle" in value:
        import aws_sdk_geo_places.types.filter_circle

        out["Circle"] = aws_sdk_geo_places.types.filter_circle.serialize_json(
            value["circle"]
        )
    if "include_countries" in value:
        import aws_sdk_geo_places.types.country_code_list

        out["IncludeCountries"] = (
            aws_sdk_geo_places.types.country_code_list.serialize_json(
                value["include_countries"]
            )
        )
    if "include_place_types" in value:
        import aws_sdk_geo_places.types.autocomplete_filter_place_type_list

        out["IncludePlaceTypes"] = (
            aws_sdk_geo_places.types.autocomplete_filter_place_type_list.serialize_json(
                value["include_place_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutocompleteFilter:
    out: AutocompleteFilter = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import aws_sdk_geo_places.types.bounding_box

        out["bounding_box"] = aws_sdk_geo_places.types.bounding_box.deserialize_json(
            data["BoundingBox"]
        )
    if "Circle" in data:
        import aws_sdk_geo_places.types.filter_circle

        out["circle"] = aws_sdk_geo_places.types.filter_circle.deserialize_json(
            data["Circle"]
        )
    if "IncludeCountries" in data:
        import aws_sdk_geo_places.types.country_code_list

        out["include_countries"] = (
            aws_sdk_geo_places.types.country_code_list.deserialize_json(
                data["IncludeCountries"]
            )
        )
    if "IncludePlaceTypes" in data:
        import aws_sdk_geo_places.types.autocomplete_filter_place_type_list

        out["include_place_types"] = (
            aws_sdk_geo_places.types.autocomplete_filter_place_type_list.deserialize_json(
                data["IncludePlaceTypes"]
            )
        )
    return out
