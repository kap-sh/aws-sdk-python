"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ListPortalsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__list_of_portal_summary
    import capo_apigatewayv2.types.__string_min1_max2048


class ListPortalsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_apigatewayv2.types.__list_of_portal_summary.__listOfPortalSummary"
    ]
    """<p>The elements from this collection.</p>"""
    next_token: NotRequired[
        "capo_apigatewayv2.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPortalsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_apigatewayv2.types.__list_of_portal_summary

        out["items"] = capo_apigatewayv2.types.__list_of_portal_summary.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPortalsResponse:
    out: ListPortalsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_apigatewayv2.types.__list_of_portal_summary

        out["items"] = (
            capo_apigatewayv2.types.__list_of_portal_summary.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
