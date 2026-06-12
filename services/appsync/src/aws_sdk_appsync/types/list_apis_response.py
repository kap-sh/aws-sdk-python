"""Generated from Smithy shape ``com.amazonaws.appsync#ListApisResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.apis
    import aws_sdk_appsync.types.pagination_token


class ListApisResponse(TypedDict):
    apis: NotRequired["aws_sdk_appsync.types.apis.Apis"]
    """<p>The <code>Api</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApisResponse) -> dict:
    out: dict = {}
    if "apis" in value:
        import aws_sdk_appsync.types.apis

        out["apis"] = aws_sdk_appsync.types.apis.serialize_json(value["apis"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApisResponse:
    out: ListApisResponse = {}  # type: ignore[typeddict-item]
    if "apis" in data:
        import aws_sdk_appsync.types.apis

        out["apis"] = aws_sdk_appsync.types.apis.deserialize_json(data["apis"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
