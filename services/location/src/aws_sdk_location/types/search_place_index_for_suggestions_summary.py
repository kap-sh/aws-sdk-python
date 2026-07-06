"""Generated from Smithy shape ``com.amazonaws.location#SearchPlaceIndexForSuggestionsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.bounding_box
    import aws_sdk_location.types.country_code_list
    import aws_sdk_location.types.filter_place_category_list
    import aws_sdk_location.types.language_tag
    import aws_sdk_location.types.position
    import aws_sdk_location.types.sensitive_string


class SearchPlaceIndexForSuggestionsSummary(TypedDict, closed=True):
    text: "aws_sdk_location.types.sensitive_string.SensitiveString"
    """<p>The free-form partial text input specified in the request.</p>"""
    bias_position: NotRequired["aws_sdk_location.types.position.Position"]
    """<p>Contains the coordinates for the optional bias position specified in the request.</p> <p>This parameter contains a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents the position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p>"""
    filter_b_box: NotRequired["aws_sdk_location.types.bounding_box.BoundingBox"]
    """<p>Contains the coordinates for the optional bounding box specified in the request.</p>"""
    filter_countries: NotRequired[
        "aws_sdk_location.types.country_code_list.CountryCodeList"
    ]
    """<p>Contains the optional country filter specified in the request.</p>"""
    max_results: NotRequired["int"]
    """<p>Contains the optional result count limit specified in the request.</p>"""
    data_source: "str"
    r"""<p>The geospatial data provider attached to the place index resource specified in the request. Values can be one of the following:</p> <ul> <li> <p>Esri</p> </li> <li> <p>Grab</p> </li> <li> <p>Here</p> </li> </ul> <p>For more information about data providers, see <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html\">Amazon Location Service data providers</a>.</p>"""
    language: NotRequired["aws_sdk_location.types.language_tag.LanguageTag"]
    r"""<p>The preferred language used to return results. Matches the language in the request. The value is a valid <a href=\"https://tools.ietf.org/search/bcp47\">BCP 47</a> language tag, for example, <code>en</code> for English.</p>"""
    filter_categories: NotRequired[
        "aws_sdk_location.types.filter_place_category_list.FilterPlaceCategoryList"
    ]
    """<p>The optional category filter specified in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPlaceIndexForSuggestionsSummary) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    if "bias_position" in value:
        import aws_sdk_location.types.position

        out["BiasPosition"] = aws_sdk_location.types.position.serialize_json(
            value["bias_position"]
        )
    if "filter_b_box" in value:
        import aws_sdk_location.types.bounding_box

        out["FilterBBox"] = aws_sdk_location.types.bounding_box.serialize_json(
            value["filter_b_box"]
        )
    if "filter_countries" in value:
        import aws_sdk_location.types.country_code_list

        out["FilterCountries"] = (
            aws_sdk_location.types.country_code_list.serialize_json(
                value["filter_countries"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    out["DataSource"] = value["data_source"]
    if "language" in value:
        out["Language"] = value["language"]
    if "filter_categories" in value:
        import aws_sdk_location.types.filter_place_category_list

        out["FilterCategories"] = (
            aws_sdk_location.types.filter_place_category_list.serialize_json(
                value["filter_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchPlaceIndexForSuggestionsSummary:
    out: SearchPlaceIndexForSuggestionsSummary = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError(
            "SearchPlaceIndexForSuggestionsSummary.text required"
        )
    if "BiasPosition" in data:
        import aws_sdk_location.types.position

        out["bias_position"] = aws_sdk_location.types.position.deserialize_json(
            data["BiasPosition"]
        )
    if "FilterBBox" in data:
        import aws_sdk_location.types.bounding_box

        out["filter_b_box"] = aws_sdk_location.types.bounding_box.deserialize_json(
            data["FilterBBox"]
        )
    if "FilterCountries" in data:
        import aws_sdk_location.types.country_code_list

        out["filter_countries"] = (
            aws_sdk_location.types.country_code_list.deserialize_json(
                data["FilterCountries"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "DataSource" in data:
        out["data_source"] = data["DataSource"]
    else:
        raise DeserializationError(
            "SearchPlaceIndexForSuggestionsSummary.data_source required"
        )
    if "Language" in data:
        out["language"] = data["Language"]
    if "FilterCategories" in data:
        import aws_sdk_location.types.filter_place_category_list

        out["filter_categories"] = (
            aws_sdk_location.types.filter_place_category_list.deserialize_json(
                data["FilterCategories"]
            )
        )
    return out
