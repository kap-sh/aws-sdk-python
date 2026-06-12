"""Generated from Smithy shape ``com.amazonaws.appsync#ListTypesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.pagination_token
    import aws_sdk_appsync.types.type_list


class ListTypesResponse(TypedDict):
    types: NotRequired["aws_sdk_appsync.types.type_list.TypeList"]
    """<p>The <code>Type</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier to pass in the next request to this operation to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTypesResponse) -> dict:
    out: dict = {}
    if "types" in value:
        import aws_sdk_appsync.types.type_list

        out["types"] = aws_sdk_appsync.types.type_list.serialize_json(value["types"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTypesResponse:
    out: ListTypesResponse = {}  # type: ignore[typeddict-item]
    if "types" in data:
        import aws_sdk_appsync.types.type_list

        out["types"] = aws_sdk_appsync.types.type_list.deserialize_json(data["types"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
