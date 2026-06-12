"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestPlaceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.access_point_list
    import aws_sdk_geo_places.types.access_restriction_list
    import aws_sdk_geo_places.types.address
    import aws_sdk_geo_places.types.bounding_box
    import aws_sdk_geo_places.types.business_chain_list
    import aws_sdk_geo_places.types.category_list
    import aws_sdk_geo_places.types.country_code3
    import aws_sdk_geo_places.types.distance_meters
    import aws_sdk_geo_places.types.food_type_list
    import aws_sdk_geo_places.types.phoneme_details
    import aws_sdk_geo_places.types.place_type
    import aws_sdk_geo_places.types.position
    import aws_sdk_geo_places.types.sensitive_string
    import aws_sdk_geo_places.types.time_zone


class SuggestPlaceResult(TypedDict):
    place_id: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The <code>PlaceId</code> of the place you wish to receive the information for.</p>"""
    place_type: NotRequired["aws_sdk_geo_places.types.place_type.PlaceType"]
    """<p>A <code>PlaceType</code> is a category that the result place must belong to.</p>"""
    address: NotRequired["aws_sdk_geo_places.types.address.Address"]
    """<p>The place's address.</p>"""
    position: NotRequired["aws_sdk_geo_places.types.position.Position"]
    """<p>The position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    distance: "aws_sdk_geo_places.types.distance_meters.DistanceMeters"
    """<p>The distance in meters from the QueryPosition.</p>"""
    map_view: NotRequired["aws_sdk_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set 4 coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    categories: NotRequired["aws_sdk_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong to.</p>"""
    food_types: NotRequired["aws_sdk_geo_places.types.food_type_list.FoodTypeList"]
    """<p> List of food types offered by this result. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    business_chains: NotRequired[
        "aws_sdk_geo_places.types.business_chain_list.BusinessChainList"
    ]
    """<p> The Business Chains associated with the place. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    access_points: NotRequired[
        "aws_sdk_geo_places.types.access_point_list.AccessPointList"
    ]
    """<p> Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude]. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    access_restrictions: NotRequired[
        "aws_sdk_geo_places.types.access_restriction_list.AccessRestrictionList"
    ]
    """<p> Indicates known access restrictions on a vehicle access point. The index correlates to an access point and indicates if access through this point has some form of restriction. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    time_zone: NotRequired["aws_sdk_geo_places.types.time_zone.TimeZone"]
    """<p>The time zone in which the place is located.</p>"""
    political_view: NotRequired["aws_sdk_geo_places.types.country_code3.CountryCode3"]
    """<p> The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    phonemes: NotRequired["aws_sdk_geo_places.types.phoneme_details.PhonemeDetails"]
    """<p> How the various components of the result's address are pronounced in various languages. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestPlaceResult) -> dict:
    out: dict = {}
    if "place_id" in value:
        out["PlaceId"] = value["place_id"]
    if "place_type" in value:
        out["PlaceType"] = value["place_type"]
    if "address" in value:
        import aws_sdk_geo_places.types.address

        out["Address"] = aws_sdk_geo_places.types.address.serialize_json(
            value["address"]
        )
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


def deserialize_json(data: dict) -> SuggestPlaceResult:
    out: SuggestPlaceResult = {}  # type: ignore[typeddict-item]
    if "PlaceId" in data:
        out["place_id"] = data["PlaceId"]
    if "PlaceType" in data:
        out["place_type"] = data["PlaceType"]
    if "Address" in data:
        import aws_sdk_geo_places.types.address

        out["address"] = aws_sdk_geo_places.types.address.deserialize_json(
            data["Address"]
        )
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
