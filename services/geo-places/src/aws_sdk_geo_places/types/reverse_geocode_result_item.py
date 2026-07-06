"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.access_point_list
    import aws_sdk_geo_places.types.address
    import aws_sdk_geo_places.types.bounding_box
    import aws_sdk_geo_places.types.category_list
    import aws_sdk_geo_places.types.country_code3
    import aws_sdk_geo_places.types.distance_meters
    import aws_sdk_geo_places.types.food_type_list
    import aws_sdk_geo_places.types.intersection_list
    import aws_sdk_geo_places.types.place_type
    import aws_sdk_geo_places.types.position
    import aws_sdk_geo_places.types.postal_code_details_list
    import aws_sdk_geo_places.types.sensitive_boolean
    import aws_sdk_geo_places.types.sensitive_string
    import aws_sdk_geo_places.types.time_zone


class ReverseGeocodeResultItem(TypedDict, closed=True):
    place_id: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The <code>PlaceId</code> of the place you wish to receive the information for.</p>"""
    place_type: "aws_sdk_geo_places.types.place_type.PlaceType"
    """<p>A <code>PlaceType</code> is a category that the result place must belong to.</p>"""
    title: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The localized display name of this result item based on request parameter <code>language</code>. </p>"""
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
    distance: "aws_sdk_geo_places.types.distance_meters.DistanceMeters"
    """<p>The distance in meters from the QueryPosition.</p>"""
    map_view: NotRequired["aws_sdk_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set 4 coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    categories: NotRequired["aws_sdk_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong to.</p>"""
    food_types: NotRequired["aws_sdk_geo_places.types.food_type_list.FoodTypeList"]
    r"""<p> List of food types offered by this result. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    access_points: NotRequired[
        "aws_sdk_geo_places.types.access_point_list.AccessPointList"
    ]
    r"""<p> Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude]. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    time_zone: NotRequired["aws_sdk_geo_places.types.time_zone.TimeZone"]
    """<p>The time zone in which the place is located.</p>"""
    political_view: NotRequired["aws_sdk_geo_places.types.country_code3.CountryCode3"]
    r"""<p> The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    intersections: NotRequired[
        "aws_sdk_geo_places.types.intersection_list.IntersectionList"
    ]
    r"""<p> All Intersections that are near the provided address. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeResultItem) -> dict:
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
    if "access_points" in value:
        import aws_sdk_geo_places.types.access_point_list

        out["AccessPoints"] = aws_sdk_geo_places.types.access_point_list.serialize_json(
            value["access_points"]
        )
    if "time_zone" in value:
        import aws_sdk_geo_places.types.time_zone

        out["TimeZone"] = aws_sdk_geo_places.types.time_zone.serialize_json(
            value["time_zone"]
        )
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "intersections" in value:
        import aws_sdk_geo_places.types.intersection_list

        out["Intersections"] = (
            aws_sdk_geo_places.types.intersection_list.serialize_json(
                value["intersections"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReverseGeocodeResultItem:
    out: ReverseGeocodeResultItem = {}  # type: ignore[typeddict-item]
    if "PlaceId" in data:
        out["place_id"] = data["PlaceId"]
    else:
        raise DeserializationError("ReverseGeocodeResultItem.place_id required")
    if "PlaceType" in data:
        out["place_type"] = data["PlaceType"]
    else:
        raise DeserializationError("ReverseGeocodeResultItem.place_type required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("ReverseGeocodeResultItem.title required")
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
    if "AccessPoints" in data:
        import aws_sdk_geo_places.types.access_point_list

        out["access_points"] = (
            aws_sdk_geo_places.types.access_point_list.deserialize_json(
                data["AccessPoints"]
            )
        )
    if "TimeZone" in data:
        import aws_sdk_geo_places.types.time_zone

        out["time_zone"] = aws_sdk_geo_places.types.time_zone.deserialize_json(
            data["TimeZone"]
        )
    if "PoliticalView" in data:
        out["political_view"] = data["PoliticalView"]
    if "Intersections" in data:
        import aws_sdk_geo_places.types.intersection_list

        out["intersections"] = (
            aws_sdk_geo_places.types.intersection_list.deserialize_json(
                data["Intersections"]
            )
        )
    return out
