"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchNearbyResultItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.access_point_list
    import aws_sdk_geo_places.types.access_restriction_list
    import aws_sdk_geo_places.types.address
    import aws_sdk_geo_places.types.bounding_box
    import aws_sdk_geo_places.types.business_chain_list
    import aws_sdk_geo_places.types.category_list
    import aws_sdk_geo_places.types.contacts
    import aws_sdk_geo_places.types.country_code3
    import aws_sdk_geo_places.types.distance_meters
    import aws_sdk_geo_places.types.food_type_list
    import aws_sdk_geo_places.types.opening_hours_list
    import aws_sdk_geo_places.types.phoneme_details
    import aws_sdk_geo_places.types.place_type
    import aws_sdk_geo_places.types.position
    import aws_sdk_geo_places.types.sensitive_boolean
    import aws_sdk_geo_places.types.sensitive_string
    import aws_sdk_geo_places.types.time_zone


class SearchNearbyResultItem(TypedDict):
    place_id: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The <code>PlaceId</code> of the place you wish to receive the information for.</p>"""
    place_type: "aws_sdk_geo_places.types.place_type.PlaceType"
    """<p>A <code>PlaceType</code> is a category that the result place must belong to.</p>"""
    title: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The item's title.</p>"""
    address: NotRequired["aws_sdk_geo_places.types.address.Address"]
    """<p>The place's address.</p>"""
    address_number_corrected: NotRequired[
        "aws_sdk_geo_places.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Boolean indicating if the address provided has been corrected.</p>"""
    position: NotRequired["aws_sdk_geo_places.types.position.Position"]
    """<p>The position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    distance: "aws_sdk_geo_places.types.distance_meters.DistanceMeters"
    """<p>The distance in meters from the QueryPosition.</p>"""
    map_view: NotRequired["aws_sdk_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set 4 coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    categories: NotRequired["aws_sdk_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong to.</p>"""
    food_types: NotRequired["aws_sdk_geo_places.types.food_type_list.FoodTypeList"]
    """<p>List of food types offered by this result.</p>"""
    business_chains: NotRequired[
        "aws_sdk_geo_places.types.business_chain_list.BusinessChainList"
    ]
    """<p>The Business Chains associated with the place.</p>"""
    contacts: NotRequired["aws_sdk_geo_places.types.contacts.Contacts"]
    """<p>List of potential contact methods for the result/place.</p>"""
    opening_hours: NotRequired[
        "aws_sdk_geo_places.types.opening_hours_list.OpeningHoursList"
    ]
    """<p>List of opening hours objects.</p>"""
    access_points: NotRequired[
        "aws_sdk_geo_places.types.access_point_list.AccessPointList"
    ]
    """<p>Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    access_restrictions: NotRequired[
        "aws_sdk_geo_places.types.access_restriction_list.AccessRestrictionList"
    ]
    """<p>Indicates known access restrictions on a vehicle access point. The index correlates to an access point and indicates if access through this point has some form of restriction.</p>"""
    time_zone: NotRequired["aws_sdk_geo_places.types.time_zone.TimeZone"]
    """<p>The time zone in which the place is located.</p>"""
    political_view: NotRequired["aws_sdk_geo_places.types.country_code3.CountryCode3"]
    """<p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.</p>"""
    phonemes: NotRequired["aws_sdk_geo_places.types.phoneme_details.PhonemeDetails"]
    """<p>How the various components of the result's address are pronounced in various languages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchNearbyResultItem) -> dict:
    out: dict = {}
    out["PlaceId"] = value["place_id"]
    out["PlaceType"] = value["place_type"]
    out["Title"] = value["title"]
    if "address" in value:
        import aws_sdk_geo_places.types.address

        out["Address"] = aws_sdk_geo_places.types.address.serialize_json(
            value["address"]
        )
    if "address_number_corrected" in value:
        out["AddressNumberCorrected"] = value["address_number_corrected"]
    if "position" in value:
        import aws_sdk_geo_places.types.position

        out["Position"] = aws_sdk_geo_places.types.position.serialize_json(
            value["position"]
        )
    out["Distance"] = value.get("distance", 0)
    if "map_view" in value:
        import aws_sdk_geo_places.types.bounding_box

        out["MapView"] = aws_sdk_geo_places.types.bounding_box.serialize_json(
            value["map_view"]
        )
    if "categories" in value:
        import aws_sdk_geo_places.types.category_list

        out["Categories"] = aws_sdk_geo_places.types.category_list.serialize_json(
            value["categories"]
        )
    if "food_types" in value:
        import aws_sdk_geo_places.types.food_type_list

        out["FoodTypes"] = aws_sdk_geo_places.types.food_type_list.serialize_json(
            value["food_types"]
        )
    if "business_chains" in value:
        import aws_sdk_geo_places.types.business_chain_list

        out["BusinessChains"] = (
            aws_sdk_geo_places.types.business_chain_list.serialize_json(
                value["business_chains"]
            )
        )
    if "contacts" in value:
        import aws_sdk_geo_places.types.contacts

        out["Contacts"] = aws_sdk_geo_places.types.contacts.serialize_json(
            value["contacts"]
        )
    if "opening_hours" in value:
        import aws_sdk_geo_places.types.opening_hours_list

        out["OpeningHours"] = (
            aws_sdk_geo_places.types.opening_hours_list.serialize_json(
                value["opening_hours"]
            )
        )
    if "access_points" in value:
        import aws_sdk_geo_places.types.access_point_list

        out["AccessPoints"] = aws_sdk_geo_places.types.access_point_list.serialize_json(
            value["access_points"]
        )
    if "access_restrictions" in value:
        import aws_sdk_geo_places.types.access_restriction_list

        out["AccessRestrictions"] = (
            aws_sdk_geo_places.types.access_restriction_list.serialize_json(
                value["access_restrictions"]
            )
        )
    if "time_zone" in value:
        import aws_sdk_geo_places.types.time_zone

        out["TimeZone"] = aws_sdk_geo_places.types.time_zone.serialize_json(
            value["time_zone"]
        )
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "phonemes" in value:
        import aws_sdk_geo_places.types.phoneme_details

        out["Phonemes"] = aws_sdk_geo_places.types.phoneme_details.serialize_json(
            value["phonemes"]
        )
    return out


def deserialize_json(data: dict) -> SearchNearbyResultItem:
    out: SearchNearbyResultItem = {}  # type: ignore[typeddict-item]
    if "PlaceId" in data:
        out["place_id"] = data["PlaceId"]
    else:
        raise DeserializationError("SearchNearbyResultItem.place_id required")
    if "PlaceType" in data:
        out["place_type"] = data["PlaceType"]
    else:
        raise DeserializationError("SearchNearbyResultItem.place_type required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("SearchNearbyResultItem.title required")
    if "Address" in data:
        import aws_sdk_geo_places.types.address

        out["address"] = aws_sdk_geo_places.types.address.deserialize_json(
            data["Address"]
        )
    if "AddressNumberCorrected" in data:
        out["address_number_corrected"] = data["AddressNumberCorrected"]
    if "Position" in data:
        import aws_sdk_geo_places.types.position

        out["position"] = aws_sdk_geo_places.types.position.deserialize_json(
            data["Position"]
        )
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "MapView" in data:
        import aws_sdk_geo_places.types.bounding_box

        out["map_view"] = aws_sdk_geo_places.types.bounding_box.deserialize_json(
            data["MapView"]
        )
    if "Categories" in data:
        import aws_sdk_geo_places.types.category_list

        out["categories"] = aws_sdk_geo_places.types.category_list.deserialize_json(
            data["Categories"]
        )
    if "FoodTypes" in data:
        import aws_sdk_geo_places.types.food_type_list

        out["food_types"] = aws_sdk_geo_places.types.food_type_list.deserialize_json(
            data["FoodTypes"]
        )
    if "BusinessChains" in data:
        import aws_sdk_geo_places.types.business_chain_list

        out["business_chains"] = (
            aws_sdk_geo_places.types.business_chain_list.deserialize_json(
                data["BusinessChains"]
            )
        )
    if "Contacts" in data:
        import aws_sdk_geo_places.types.contacts

        out["contacts"] = aws_sdk_geo_places.types.contacts.deserialize_json(
            data["Contacts"]
        )
    if "OpeningHours" in data:
        import aws_sdk_geo_places.types.opening_hours_list

        out["opening_hours"] = (
            aws_sdk_geo_places.types.opening_hours_list.deserialize_json(
                data["OpeningHours"]
            )
        )
    if "AccessPoints" in data:
        import aws_sdk_geo_places.types.access_point_list

        out["access_points"] = (
            aws_sdk_geo_places.types.access_point_list.deserialize_json(
                data["AccessPoints"]
            )
        )
    if "AccessRestrictions" in data:
        import aws_sdk_geo_places.types.access_restriction_list

        out["access_restrictions"] = (
            aws_sdk_geo_places.types.access_restriction_list.deserialize_json(
                data["AccessRestrictions"]
            )
        )
    if "TimeZone" in data:
        import aws_sdk_geo_places.types.time_zone

        out["time_zone"] = aws_sdk_geo_places.types.time_zone.deserialize_json(
            data["TimeZone"]
        )
    if "PoliticalView" in data:
        out["political_view"] = data["PoliticalView"]
    if "Phonemes" in data:
        import aws_sdk_geo_places.types.phoneme_details

        out["phonemes"] = aws_sdk_geo_places.types.phoneme_details.deserialize_json(
            data["Phonemes"]
        )
    return out
