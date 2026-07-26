"""Generated from Smithy shape ``com.amazonaws.appsync#ListFunctionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.functions
    import capo_appsync.types.pagination_token


class ListFunctionsResponse(TypedDict, closed=True):
    functions: NotRequired["capo_appsync.types.functions.Functions"]
    """<p>A list of <code>Function</code> objects.</p>"""
    next_token: NotRequired["capo_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsResponse) -> dict:
    out: dict = {}
    if "functions" in value:
        import capo_appsync.types.functions

        out["functions"] = capo_appsync.types.functions.serialize_json(
            value["functions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFunctionsResponse:
    out: ListFunctionsResponse = {}  # type: ignore[typeddict-item]
    if "functions" in data:
        import capo_appsync.types.functions

        out["functions"] = capo_appsync.types.functions.deserialize_json(
            data["functions"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
