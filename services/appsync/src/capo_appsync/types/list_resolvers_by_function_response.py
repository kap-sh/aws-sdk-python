"""Generated from Smithy shape ``com.amazonaws.appsync#ListResolversByFunctionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.pagination_token
    import capo_appsync.types.resolvers


class ListResolversByFunctionResponse(TypedDict, closed=True):
    resolvers: NotRequired["capo_appsync.types.resolvers.Resolvers"]
    """<p>The list of resolvers.</p>"""
    next_token: NotRequired["capo_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier that you can use to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResolversByFunctionResponse) -> dict:
    out: dict = {}
    if "resolvers" in value:
        import capo_appsync.types.resolvers

        out["resolvers"] = capo_appsync.types.resolvers.serialize_json(
            value["resolvers"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResolversByFunctionResponse:
    out: ListResolversByFunctionResponse = {}  # type: ignore[typeddict-item]
    if "resolvers" in data:
        import capo_appsync.types.resolvers

        out["resolvers"] = capo_appsync.types.resolvers.deserialize_json(
            data["resolvers"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
