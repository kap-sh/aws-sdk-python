"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetDomainNamesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of_domain_name
    import aws_sdk_apigatewayv2.types.next_token


class GetDomainNamesResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_domain_name.__listOfDomainName"
    ]
    """<p>The elements from this collection.</p>"""
    next_token: NotRequired["aws_sdk_apigatewayv2.types.next_token.NextToken"]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainNamesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_apigatewayv2.types.__list_of_domain_name

        out["items"] = aws_sdk_apigatewayv2.types.__list_of_domain_name.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDomainNamesResponse:
    out: GetDomainNamesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_apigatewayv2.types.__list_of_domain_name

        out["items"] = (
            aws_sdk_apigatewayv2.types.__list_of_domain_name.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
