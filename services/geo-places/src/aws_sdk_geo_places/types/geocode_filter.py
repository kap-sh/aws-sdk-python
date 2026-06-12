"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.country_code_list
    import aws_sdk_geo_places.types.geocode_filter_place_type_list


class GeocodeFilter(TypedDict):
    include_countries: NotRequired[
        "aws_sdk_geo_places.types.country_code_list.CountryCodeList"
    ]
    """<p> A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.</p>"""
    include_place_types: NotRequired[
        "aws_sdk_geo_places.types.geocode_filter_place_type_list.GeocodeFilterPlaceTypeList"
    ]
    """<p>The included place types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeFilter) -> dict:
    out: dict = {}
    if "include_countries" in value:
        import aws_sdk_geo_places.types.country_code_list

        out["IncludeCountries"] = (
            aws_sdk_geo_places.types.country_code_list.serialize_json(
                value["include_countries"]
            )
        )
    if "include_place_types" in value:
        import aws_sdk_geo_places.types.geocode_filter_place_type_list

        out["IncludePlaceTypes"] = (
            aws_sdk_geo_places.types.geocode_filter_place_type_list.serialize_json(
                value["include_place_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeocodeFilter:
    out: GeocodeFilter = {}  # type: ignore[typeddict-item]
    if "IncludeCountries" in data:
        import aws_sdk_geo_places.types.country_code_list

        out["include_countries"] = (
            aws_sdk_geo_places.types.country_code_list.deserialize_json(
                data["IncludeCountries"]
            )
        )
    if "IncludePlaceTypes" in data:
        import aws_sdk_geo_places.types.geocode_filter_place_type_list

        out["include_place_types"] = (
            aws_sdk_geo_places.types.geocode_filter_place_type_list.deserialize_json(
                data["IncludePlaceTypes"]
            )
        )
    return out
