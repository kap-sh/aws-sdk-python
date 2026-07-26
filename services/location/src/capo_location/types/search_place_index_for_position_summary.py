"""Generated from Smithy shape ``com.amazonaws.location#SearchPlaceIndexForPositionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.language_tag
    import capo_location.types.place_index_search_result_limit
    import capo_location.types.position


class SearchPlaceIndexForPositionSummary(TypedDict, closed=True):
    position: "capo_location.types.position.Position"
    """<p>The position specified in the request.</p>"""
    max_results: NotRequired[
        "capo_location.types.place_index_search_result_limit.PlaceIndexSearchResultLimit"
    ]
    """<p>Contains the optional result count limit that is specified in the request.</p> <p>Default value: <code>50</code> </p>"""
    data_source: "str"
    r"""<p>The geospatial data provider attached to the place index resource specified in the request. Values can be one of the following:</p> <ul> <li> <p>Esri</p> </li> <li> <p>Grab</p> </li> <li> <p>Here</p> </li> </ul> <p>For more information about data providers, see <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html\">Amazon Location Service data providers</a>.</p>"""
    language: NotRequired["capo_location.types.language_tag.LanguageTag"]
    r"""<p>The preferred language used to return results. Matches the language in the request. The value is a valid <a href=\"https://tools.ietf.org/search/bcp47\">BCP 47</a> language tag, for example, <code>en</code> for English.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPlaceIndexForPositionSummary) -> dict:
    out: dict = {}
    import capo_location.types.position

    out["Position"] = capo_location.types.position.serialize_json(value["position"])
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    out["DataSource"] = value["data_source"]
    if "language" in value:
        out["Language"] = value["language"]
    return out


def deserialize_json(data: dict) -> SearchPlaceIndexForPositionSummary:
    out: SearchPlaceIndexForPositionSummary = {}  # type: ignore[typeddict-item]
    if "Position" in data:
        import capo_location.types.position

        out["position"] = capo_location.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError(
            "SearchPlaceIndexForPositionSummary.position required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "DataSource" in data:
        out["data_source"] = data["DataSource"]
    else:
        raise DeserializationError(
            "SearchPlaceIndexForPositionSummary.data_source required"
        )
    if "Language" in data:
        out["language"] = data["Language"]
    return out
