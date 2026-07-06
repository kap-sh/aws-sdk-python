"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.address
    import aws_sdk_geo_places.types.autocomplete_highlights
    import aws_sdk_geo_places.types.country_code3
    import aws_sdk_geo_places.types.distance_meters
    import aws_sdk_geo_places.types.language_tag
    import aws_sdk_geo_places.types.place_type
    import aws_sdk_geo_places.types.sensitive_string


class AutocompleteResultItem(TypedDict, closed=True):
    place_id: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The PlaceId of the place associated with this result. This can be used to look up additional details about the result via GetPlace.</p>"""
    place_type: "aws_sdk_geo_places.types.place_type.PlaceType"
    """<p>PlaceType describes the type of result entry returned.</p>"""
    title: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>A formatted string for display when presenting this result to an end user.</p>"""
    address: NotRequired["aws_sdk_geo_places.types.address.Address"]
    """<p>The address associated with this result.</p>"""
    distance: "aws_sdk_geo_places.types.distance_meters.DistanceMeters"
    """<p>The distance in meters between the center of the search area and this result. Useful to evaluate how far away from the original bias position the result is.</p>"""
    language: NotRequired["aws_sdk_geo_places.types.language_tag.LanguageTag"]
    r"""<p>A list of <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>"""
    political_view: NotRequired["aws_sdk_geo_places.types.country_code3.CountryCode3"]
    """<p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.</p>"""
    highlights: NotRequired[
        "aws_sdk_geo_places.types.autocomplete_highlights.AutocompleteHighlights"
    ]
    """<p>Indicates the starting and ending index of the place in the text query that match the found title. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteResultItem) -> dict:
    out: dict = {}
    out["PlaceId"] = value["place_id"]
    out["PlaceType"] = value["place_type"]
    out["Title"] = value["title"]
    if "address" in value:
        import aws_sdk_geo_places.types.address

        out["Address"] = aws_sdk_geo_places.types.address.serialize_json(
            value["address"]
        )
    out["Distance"] = value.get("distance", 0)
    if "language" in value:
        out["Language"] = value["language"]
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "highlights" in value:
        import aws_sdk_geo_places.types.autocomplete_highlights

        out["Highlights"] = (
            aws_sdk_geo_places.types.autocomplete_highlights.serialize_json(
                value["highlights"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutocompleteResultItem:
    out: AutocompleteResultItem = {}  # type: ignore[typeddict-item]
    if "PlaceId" in data:
        out["place_id"] = data["PlaceId"]
    else:
        raise DeserializationError("AutocompleteResultItem.place_id required")
    if "PlaceType" in data:
        out["place_type"] = data["PlaceType"]
    else:
        raise DeserializationError("AutocompleteResultItem.place_type required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("AutocompleteResultItem.title required")
    if "Address" in data:
        import aws_sdk_geo_places.types.address

        out["address"] = aws_sdk_geo_places.types.address.deserialize_json(
            data["Address"]
        )
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "Language" in data:
        out["language"] = data["Language"]
    if "PoliticalView" in data:
        out["political_view"] = data["PoliticalView"]
    if "Highlights" in data:
        import aws_sdk_geo_places.types.autocomplete_highlights

        out["highlights"] = (
            aws_sdk_geo_places.types.autocomplete_highlights.deserialize_json(
                data["Highlights"]
            )
        )
    return out
