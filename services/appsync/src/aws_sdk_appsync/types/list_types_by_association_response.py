"""Generated from Smithy shape ``com.amazonaws.appsync#ListTypesByAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.pagination_token
    import aws_sdk_appsync.types.type_list


class ListTypesByAssociationResponse(TypedDict, closed=True):
    types: NotRequired["aws_sdk_appsync.types.type_list.TypeList"]
    """<p>The <code>Type</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTypesByAssociationResponse) -> dict:
    out: dict = {}
    if "types" in value:
        import aws_sdk_appsync.types.type_list

        out["types"] = aws_sdk_appsync.types.type_list.serialize_json(value["types"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTypesByAssociationResponse:
    out: ListTypesByAssociationResponse = {}  # type: ignore[typeddict-item]
    if "types" in data:
        import aws_sdk_appsync.types.type_list

        out["types"] = aws_sdk_appsync.types.type_list.deserialize_json(data["types"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
