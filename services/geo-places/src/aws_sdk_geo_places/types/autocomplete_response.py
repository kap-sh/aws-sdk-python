"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.autocomplete_result_item_list


class AutocompleteResponse(TypedDict, closed=True):
    pricing_bucket: "str"
    r"""<p>The pricing bucket for which the query is charged at.</p> <p>For more information on pricing, please visit <a href=\"https://aws.amazon.com/location/pricing/\">Amazon Location Service Pricing</a>.</p>"""
    result_items: NotRequired[
        "aws_sdk_geo_places.types.autocomplete_result_item_list.AutocompleteResultItemList"
    ]
    """<p>List of places or results returned for a query. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteResponse) -> dict:
    out: dict = {}
    if "result_items" in value:
        import aws_sdk_geo_places.types.autocomplete_result_item_list

        out["ResultItems"] = (
            aws_sdk_geo_places.types.autocomplete_result_item_list.serialize_json(
                value["result_items"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutocompleteResponse:
    out: AutocompleteResponse = {}  # type: ignore[typeddict-item]
    if "ResultItems" in data:
        import aws_sdk_geo_places.types.autocomplete_result_item_list

        out["result_items"] = (
            aws_sdk_geo_places.types.autocomplete_result_item_list.deserialize_json(
                data["ResultItems"]
            )
        )
    return out
