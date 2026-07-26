"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.access_point_list
    import capo_geo_places.types.address
    import capo_geo_places.types.bounding_box
    import capo_geo_places.types.category_list
    import capo_geo_places.types.country_code3
    import capo_geo_places.types.distance_meters
    import capo_geo_places.types.food_type_list
    import capo_geo_places.types.geocode_parsed_query
    import capo_geo_places.types.intersection_list
    import capo_geo_places.types.match_score_details
    import capo_geo_places.types.place_type
    import capo_geo_places.types.position
    import capo_geo_places.types.postal_code_details_list
    import capo_geo_places.types.related_place
    import capo_geo_places.types.related_place_list
    import capo_geo_places.types.sensitive_boolean
    import capo_geo_places.types.sensitive_string
    import capo_geo_places.types.time_zone


class GeocodeResultItem(TypedDict, closed=True):
    place_id: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The <code>PlaceId</code> of the place result.</p>"""
    place_type: "capo_geo_places.types.place_type.PlaceType"
    """<p>A <code>PlaceType</code> is a category that the result place must belong to.</p>"""
    title: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The localized display name of this result item based on request parameter <code>language</code>. </p>"""
    address: NotRequired["capo_geo_places.types.address.Address"]
    """<p>The place's address.</p>"""
    address_number_corrected: NotRequired[
        "capo_geo_places.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Boolean indicating if the address provided has been corrected.</p>"""
    postal_code_details: NotRequired[
        "capo_geo_places.types.postal_code_details_list.PostalCodeDetailsList"
    ]
    """<p>Contains details about the postal code of the place/result. </p>"""
    position: NotRequired["capo_geo_places.types.position.Position"]
    """<p>The position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    distance: "capo_geo_places.types.distance_meters.DistanceMeters"
    """<p>The distance in meters from the QueryPosition.</p>"""
    map_view: NotRequired["capo_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set 4 coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    categories: NotRequired["capo_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong to.</p>"""
    food_types: NotRequired["capo_geo_places.types.food_type_list.FoodTypeList"]
    """<p>List of food types offered by this result.</p>"""
    access_points: NotRequired[
        "capo_geo_places.types.access_point_list.AccessPointList"
    ]
    """<p>Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    time_zone: NotRequired["capo_geo_places.types.time_zone.TimeZone"]
    """<p>The time zone in which the place is located.</p>"""
    political_view: NotRequired["capo_geo_places.types.country_code3.CountryCode3"]
    """<p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.</p>"""
    match_scores: NotRequired[
        "capo_geo_places.types.match_score_details.MatchScoreDetails"
    ]
    """<p>Indicates how well the entire input matches the returned. It is equal to 1 if all input tokens are recognized and matched.</p>"""
    parsed_query: NotRequired[
        "capo_geo_places.types.geocode_parsed_query.GeocodeParsedQuery"
    ]
    """<p>Free-form text query.</p>"""
    intersections: NotRequired[
        "capo_geo_places.types.intersection_list.IntersectionList"
    ]
    """<p>All Intersections that are near the provided address.</p>"""
    main_address: NotRequired["capo_geo_places.types.related_place.RelatedPlace"]
    """<p>The main address corresponding to a place of type Secondary Address.</p>"""
    secondary_addresses: NotRequired[
        "capo_geo_places.types.related_place_list.RelatedPlaceList"
    ]
    """<p>All secondary addresses that are associated with a main address. A secondary address is one that includes secondary designators, such as a Suite or Unit Number, Building, or Floor information.</p> <note> <p>Coverage for this functionality is available in the following countries: AUS, CAN, NZL, USA, PRI.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeResultItem) -> dict:
    out: dict = {}
    out["PlaceId"] = value["place_id"]
    out["PlaceType"] = value["place_type"]
    out["Title"] = value["title"]
    if "address" in value:
        import capo_geo_places.types.address

        out["Address"] = capo_geo_places.types.address.serialize_json(value["address"])
    if "address_number_corrected" in value:
        out["AddressNumberCorrected"] = value["address_number_corrected"]
    if "postal_code_details" in value:
        import capo_geo_places.types.postal_code_details_list

        out["PostalCodeDetails"] = (
            capo_geo_places.types.postal_code_details_list.serialize_json(
                value["postal_code_details"]
            )
        )
    if "position" in value:
        import capo_geo_places.types.position

        out["Position"] = capo_geo_places.types.position.serialize_json(
            value["position"]
        )
    out["Distance"] = value.get("distance", 0)
    if "map_view" in value:
        import capo_geo_places.types.bounding_box

        out["MapView"] = capo_geo_places.types.bounding_box.serialize_json(
            value["map_view"]
        )
    if "categories" in value:
        import capo_geo_places.types.category_list

        out["Categories"] = capo_geo_places.types.category_list.serialize_json(
            value["categories"]
        )
    if "food_types" in value:
        import capo_geo_places.types.food_type_list

        out["FoodTypes"] = capo_geo_places.types.food_type_list.serialize_json(
            value["food_types"]
        )
    if "access_points" in value:
        import capo_geo_places.types.access_point_list

        out["AccessPoints"] = capo_geo_places.types.access_point_list.serialize_json(
            value["access_points"]
        )
    if "time_zone" in value:
        import capo_geo_places.types.time_zone

        out["TimeZone"] = capo_geo_places.types.time_zone.serialize_json(
            value["time_zone"]
        )
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "match_scores" in value:
        import capo_geo_places.types.match_score_details

        out["MatchScores"] = capo_geo_places.types.match_score_details.serialize_json(
            value["match_scores"]
        )
    if "parsed_query" in value:
        import capo_geo_places.types.geocode_parsed_query

        out["ParsedQuery"] = capo_geo_places.types.geocode_parsed_query.serialize_json(
            value["parsed_query"]
        )
    if "intersections" in value:
        import capo_geo_places.types.intersection_list

        out["Intersections"] = capo_geo_places.types.intersection_list.serialize_json(
            value["intersections"]
        )
    if "main_address" in value:
        import capo_geo_places.types.related_place

        out["MainAddress"] = capo_geo_places.types.related_place.serialize_json(
            value["main_address"]
        )
    if "secondary_addresses" in value:
        import capo_geo_places.types.related_place_list

        out["SecondaryAddresses"] = (
            capo_geo_places.types.related_place_list.serialize_json(
                value["secondary_addresses"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeocodeResultItem:
    out: GeocodeResultItem = {}  # type: ignore[typeddict-item]
    if "PlaceId" in data:
        out["place_id"] = data["PlaceId"]
    else:
        raise DeserializationError("GeocodeResultItem.place_id required")
    if "PlaceType" in data:
        out["place_type"] = data["PlaceType"]
    else:
        raise DeserializationError("GeocodeResultItem.place_type required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("GeocodeResultItem.title required")
    if "Address" in data:
        import capo_geo_places.types.address

        out["address"] = capo_geo_places.types.address.deserialize_json(data["Address"])
    if "AddressNumberCorrected" in data:
        out["address_number_corrected"] = data["AddressNumberCorrected"]
    if "PostalCodeDetails" in data:
        import capo_geo_places.types.postal_code_details_list

        out["postal_code_details"] = (
            capo_geo_places.types.postal_code_details_list.deserialize_json(
                data["PostalCodeDetails"]
            )
        )
    if "Position" in data:
        import capo_geo_places.types.position

        out["position"] = capo_geo_places.types.position.deserialize_json(
            data["Position"]
        )
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "MapView" in data:
        import capo_geo_places.types.bounding_box

        out["map_view"] = capo_geo_places.types.bounding_box.deserialize_json(
            data["MapView"]
        )
    if "Categories" in data:
        import capo_geo_places.types.category_list

        out["categories"] = capo_geo_places.types.category_list.deserialize_json(
            data["Categories"]
        )
    if "FoodTypes" in data:
        import capo_geo_places.types.food_type_list

        out["food_types"] = capo_geo_places.types.food_type_list.deserialize_json(
            data["FoodTypes"]
        )
    if "AccessPoints" in data:
        import capo_geo_places.types.access_point_list

        out["access_points"] = capo_geo_places.types.access_point_list.deserialize_json(
            data["AccessPoints"]
        )
    if "TimeZone" in data:
        import capo_geo_places.types.time_zone

        out["time_zone"] = capo_geo_places.types.time_zone.deserialize_json(
            data["TimeZone"]
        )
    if "PoliticalView" in data:
        out["political_view"] = data["PoliticalView"]
    if "MatchScores" in data:
        import capo_geo_places.types.match_score_details

        out["match_scores"] = (
            capo_geo_places.types.match_score_details.deserialize_json(
                data["MatchScores"]
            )
        )
    if "ParsedQuery" in data:
        import capo_geo_places.types.geocode_parsed_query

        out["parsed_query"] = (
            capo_geo_places.types.geocode_parsed_query.deserialize_json(
                data["ParsedQuery"]
            )
        )
    if "Intersections" in data:
        import capo_geo_places.types.intersection_list

        out["intersections"] = capo_geo_places.types.intersection_list.deserialize_json(
            data["Intersections"]
        )
    if "MainAddress" in data:
        import capo_geo_places.types.related_place

        out["main_address"] = capo_geo_places.types.related_place.deserialize_json(
            data["MainAddress"]
        )
    if "SecondaryAddresses" in data:
        import capo_geo_places.types.related_place_list

        out["secondary_addresses"] = (
            capo_geo_places.types.related_place_list.deserialize_json(
                data["SecondaryAddresses"]
            )
        )
    return out
