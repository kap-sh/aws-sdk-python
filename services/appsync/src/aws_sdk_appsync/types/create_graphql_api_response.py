"""Generated from Smithy shape ``com.amazonaws.appsync#CreateGraphqlApiResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.graphql_api


class CreateGraphqlApiResponse(TypedDict, closed=True):
    graphql_api: NotRequired["aws_sdk_appsync.types.graphql_api.GraphqlApi"]
    """<p>The <code>GraphqlApi</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGraphqlApiResponse) -> dict:
    out: dict = {}
    if "graphql_api" in value:
        import aws_sdk_appsync.types.graphql_api

        out["graphqlApi"] = aws_sdk_appsync.types.graphql_api.serialize_json(
            value["graphql_api"]
        )
    return out


def deserialize_json(data: dict) -> CreateGraphqlApiResponse:
    out: CreateGraphqlApiResponse = {}  # type: ignore[typeddict-item]
    if "graphqlApi" in data:
        import aws_sdk_appsync.types.graphql_api

        out["graphql_api"] = aws_sdk_appsync.types.graphql_api.deserialize_json(
            data["graphqlApi"]
        )
    return out
