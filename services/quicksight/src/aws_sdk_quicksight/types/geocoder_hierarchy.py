"""Generated from Smithy shape ``com.amazonaws.quicksight#GeocoderHierarchy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geocoder_hierarchy_city_string
    import aws_sdk_quicksight.types.geocoder_hierarchy_country_string
    import aws_sdk_quicksight.types.geocoder_hierarchy_county_string
    import aws_sdk_quicksight.types.geocoder_hierarchy_post_code_string
    import aws_sdk_quicksight.types.geocoder_hierarchy_state_string


class GeocoderHierarchy(TypedDict, closed=True):
    country: NotRequired[
        "aws_sdk_quicksight.types.geocoder_hierarchy_country_string.GeocoderHierarchyCountryString"
    ]
    """<p>The country value for the preference hierarchy.</p>"""
    state: NotRequired[
        "aws_sdk_quicksight.types.geocoder_hierarchy_state_string.GeocoderHierarchyStateString"
    ]
    """<p>The state/region value for the preference hierarchy.</p>"""
    county: NotRequired[
        "aws_sdk_quicksight.types.geocoder_hierarchy_county_string.GeocoderHierarchyCountyString"
    ]
    """<p>The county/district value for the preference hierarchy.</p>"""
    city: NotRequired[
        "aws_sdk_quicksight.types.geocoder_hierarchy_city_string.GeocoderHierarchyCityString"
    ]
    """<p>The city value for the preference hierarchy.</p>"""
    post_code: NotRequired[
        "aws_sdk_quicksight.types.geocoder_hierarchy_post_code_string.GeocoderHierarchyPostCodeString"
    ]
    """<p>The postcode value for the preference hierarchy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeocoderHierarchy) -> dict:
    out: dict = {}
    if "country" in value:
        out["Country"] = value["country"]
    if "state" in value:
        out["State"] = value["state"]
    if "county" in value:
        out["County"] = value["county"]
    if "city" in value:
        out["City"] = value["city"]
    if "post_code" in value:
        out["PostCode"] = value["post_code"]
    return out


def deserialize_json(data: dict) -> GeocoderHierarchy:
    out: GeocoderHierarchy = {}  # type: ignore[typeddict-item]
    if "Country" in data:
        out["country"] = data["Country"]
    if "State" in data:
        out["state"] = data["State"]
    if "County" in data:
        out["county"] = data["County"]
    if "City" in data:
        out["city"] = data["City"]
    if "PostCode" in data:
        out["post_code"] = data["PostCode"]
    return out
