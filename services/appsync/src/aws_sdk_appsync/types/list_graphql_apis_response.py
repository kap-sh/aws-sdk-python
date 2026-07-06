"""Generated from Smithy shape ``com.amazonaws.appsync#ListGraphqlApisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.graphql_apis
    import aws_sdk_appsync.types.pagination_token


class ListGraphqlApisResponse(TypedDict, closed=True):
    graphql_apis: NotRequired["aws_sdk_appsync.types.graphql_apis.GraphqlApis"]
    """<p>The <code>GraphqlApi</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier to pass in the next request to this operation to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGraphqlApisResponse) -> dict:
    out: dict = {}
    if "graphql_apis" in value:
        import aws_sdk_appsync.types.graphql_apis

        out["graphqlApis"] = aws_sdk_appsync.types.graphql_apis.serialize_json(
            value["graphql_apis"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGraphqlApisResponse:
    out: ListGraphqlApisResponse = {}  # type: ignore[typeddict-item]
    if "graphqlApis" in data:
        import aws_sdk_appsync.types.graphql_apis

        out["graphql_apis"] = aws_sdk_appsync.types.graphql_apis.deserialize_json(
            data["graphqlApis"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
