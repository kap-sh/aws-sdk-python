"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetDeploymentsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of_deployment
    import aws_sdk_apigatewayv2.types.next_token


class GetDeploymentsResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of_deployment.__listOfDeployment"
    ]
    """<p>The elements from this collection.</p>"""
    next_token: NotRequired["aws_sdk_apigatewayv2.types.next_token.NextToken"]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_apigatewayv2.types.__list_of_deployment

        out["items"] = aws_sdk_apigatewayv2.types.__list_of_deployment.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDeploymentsResponse:
    out: GetDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_apigatewayv2.types.__list_of_deployment

        out["items"] = aws_sdk_apigatewayv2.types.__list_of_deployment.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
