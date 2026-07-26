"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeParsedQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.geocode_parsed_query_address_components
    import capo_geo_places.types.parsed_query_component_list


class GeocodeParsedQuery(TypedDict, closed=True):
    title: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The localized display name of this result item based on request parameter <code>language</code>.</p>"""
    address: NotRequired[
        "capo_geo_places.types.geocode_parsed_query_address_components.GeocodeParsedQueryAddressComponents"
    ]
    """<p>The place address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeParsedQuery) -> dict:
    out: dict = {}
    if "title" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["Title"] = capo_geo_places.types.parsed_query_component_list.serialize_json(
            value["title"]
        )
    if "address" in value:
        import capo_geo_places.types.geocode_parsed_query_address_components

        out["Address"] = (
            capo_geo_places.types.geocode_parsed_query_address_components.serialize_json(
                value["address"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeocodeParsedQuery:
    out: GeocodeParsedQuery = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        import capo_geo_places.types.parsed_query_component_list

        out["title"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Title"]
            )
        )
    if "Address" in data:
        import capo_geo_places.types.geocode_parsed_query_address_components

        out["address"] = (
            capo_geo_places.types.geocode_parsed_query_address_components.deserialize_json(
                data["Address"]
            )
        )
    return out
