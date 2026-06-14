"""Generated from Smithy shape ``com.amazonaws.geoplaces#GetPlaceResponse``."""

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
    import aws_sdk_geo_places.types.food_type_list
    import aws_sdk_geo_places.types.opening_hours_list
    import aws_sdk_geo_places.types.phoneme_details
    import aws_sdk_geo_places.types.place_type
    import aws_sdk_geo_places.types.position
    import aws_sdk_geo_places.types.postal_code_details_list
    import aws_sdk_geo_places.types.related_place
    import aws_sdk_geo_places.types.related_place_list
    import aws_sdk_geo_places.types.sensitive_boolean
    import aws_sdk_geo_places.types.sensitive_string
    import aws_sdk_geo_places.types.time_zone


class GetPlaceResponse(TypedDict):
    place_id: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The <code>PlaceId</code> of the place you wish to receive the information for.</p>"""
    place_type: "aws_sdk_geo_places.types.place_type.PlaceType"
    """<p>A <code>PlaceType</code> is a category that the result place must belong to.</p>"""
    title: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The localized display name of this result item based on request parameter <code>language</code>.</p>"""
    pricing_bucket: "str"
    r"""<p>The pricing bucket for which the query is charged at.</p> <p>For more information on pricing, please visit <a href=\"https://aws.amazon.com/location/pricing/\">Amazon Location Service Pricing</a>.</p>"""
    address: NotRequired["aws_sdk_geo_places.types.address.Address"]
    """<p>The place's address.</p>"""
    address_number_corrected: NotRequired[
        "aws_sdk_geo_places.types.sensitive_boolean.SensitiveBoolean"
    ]
    r"""<p> Boolean indicating if the address provided has been corrected. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    postal_code_details: NotRequired[
        "aws_sdk_geo_places.types.postal_code_details_list.PostalCodeDetailsList"
    ]
    r"""<p> Contains details about the postal code of the place/result. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    position: NotRequired["aws_sdk_geo_places.types.position.Position"]
    """<p>The position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    map_view: NotRequired["aws_sdk_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set of four coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    categories: NotRequired["aws_sdk_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong to.</p>"""
    food_types: NotRequired["aws_sdk_geo_places.types.food_type_list.FoodTypeList"]
    r"""<p> List of food types offered by this result. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    business_chains: NotRequired[
        "aws_sdk_geo_places.types.business_chain_list.BusinessChainList"
    ]
    """<p>The Business Chains associated with the place.</p>"""
    contacts: NotRequired["aws_sdk_geo_places.types.contacts.Contacts"]
    r"""<p> List of potential contact methods for the result/place. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    opening_hours: NotRequired[
        "aws_sdk_geo_places.types.opening_hours_list.OpeningHoursList"
    ]
    r"""<p> List of opening hours objects. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    access_points: NotRequired[
        "aws_sdk_geo_places.types.access_point_list.AccessPointList"
    ]
    r"""<p> Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude]. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    access_restrictions: NotRequired[
        "aws_sdk_geo_places.types.access_restriction_list.AccessRestrictionList"
    ]
    r"""<p> Indicates known access restrictions on a vehicle access point. The index correlates to an access point and indicates if access through this point has some form of restriction. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    time_zone: NotRequired["aws_sdk_geo_places.types.time_zone.TimeZone"]
    """<p>The time zone in which the place is located.</p>"""
    political_view: NotRequired["aws_sdk_geo_places.types.country_code3.CountryCode3"]
    r"""<p> The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    phonemes: NotRequired["aws_sdk_geo_places.types.phoneme_details.PhonemeDetails"]
    r"""<p> How the various components of the result's address are pronounced in various languages. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    main_address: NotRequired["aws_sdk_geo_places.types.related_place.RelatedPlace"]
    r"""<p> The main address corresponding to a place of type Secondary Address. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    secondary_addresses: NotRequired[
        "aws_sdk_geo_places.types.related_place_list.RelatedPlaceList"
    ]
    r"""<p> All secondary addresses that are associated with a main address. A secondary address is one that includes secondary designators, such as a Suite or Unit Number, Building, or Floor information. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <note> <p>Coverage for this functionality is available in the following countries: AUS, CAN, NZL, USA, PRI.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceResponse) -> dict:
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
    if "postal_code_details" in value:
        import aws_sdk_geo_places.types.postal_code_details_list

        out["PostalCodeDetails"] = (
            aws_sdk_geo_places.types.postal_code_details_list.serialize_json(
                value["postal_code_details"]
            )
        )
    if "position" in value:
        import aws_sdk_geo_places.types.position

        out["Position"] = aws_sdk_geo_places.types.position.serialize_json(
            value["position"]
        )
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
    if "main_address" in value:
        import aws_sdk_geo_places.types.related_place

        out["MainAddress"] = aws_sdk_geo_places.types.related_place.serialize_json(
            value["main_address"]
        )
    if "secondary_addresses" in value:
        import aws_sdk_geo_places.types.related_place_list

        out["SecondaryAddresses"] = (
            aws_sdk_geo_places.types.related_place_list.serialize_json(
                value["secondary_addresses"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPlaceResponse:
    out: GetPlaceResponse = {}  # type: ignore[typeddict-item]
    if "PlaceId" in data:
        out["place_id"] = data["PlaceId"]
    else:
        raise DeserializationError("GetPlaceResponse.place_id required")
    if "PlaceType" in data:
        out["place_type"] = data["PlaceType"]
    else:
        raise DeserializationError("GetPlaceResponse.place_type required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("GetPlaceResponse.title required")
    if "Address" in data:
        import aws_sdk_geo_places.types.address

        out["address"] = aws_sdk_geo_places.types.address.deserialize_json(
            data["Address"]
        )
    if "AddressNumberCorrected" in data:
        out["address_number_corrected"] = data["AddressNumberCorrected"]
    if "PostalCodeDetails" in data:
        import aws_sdk_geo_places.types.postal_code_details_list

        out["postal_code_details"] = (
            aws_sdk_geo_places.types.postal_code_details_list.deserialize_json(
                data["PostalCodeDetails"]
            )
        )
    if "Position" in data:
        import aws_sdk_geo_places.types.position

        out["position"] = aws_sdk_geo_places.types.position.deserialize_json(
            data["Position"]
        )
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
    if "MainAddress" in data:
        import aws_sdk_geo_places.types.related_place

        out["main_address"] = aws_sdk_geo_places.types.related_place.deserialize_json(
            data["MainAddress"]
        )
    if "SecondaryAddresses" in data:
        import aws_sdk_geo_places.types.related_place_list

        out["secondary_addresses"] = (
            aws_sdk_geo_places.types.related_place_list.deserialize_json(
                data["SecondaryAddresses"]
            )
        )
    return out
