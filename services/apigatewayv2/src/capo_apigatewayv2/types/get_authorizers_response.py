"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetAuthorizersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__list_of_authorizer
    import capo_apigatewayv2.types.next_token


class GetAuthorizersResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_apigatewayv2.types.__list_of_authorizer.__listOfAuthorizer"
    ]
    """<p>The elements from this collection.</p>"""
    next_token: NotRequired["capo_apigatewayv2.types.next_token.NextToken"]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAuthorizersResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_apigatewayv2.types.__list_of_authorizer

        out["items"] = capo_apigatewayv2.types.__list_of_authorizer.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetAuthorizersResponse:
    out: GetAuthorizersResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_apigatewayv2.types.__list_of_authorizer

        out["items"] = capo_apigatewayv2.types.__list_of_authorizer.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
