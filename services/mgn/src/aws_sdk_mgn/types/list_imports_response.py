"""Generated from Smithy shape ``com.amazonaws.mgn#ListImportsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.import_list
    import aws_sdk_mgn.types.pagination_token


class ListImportsResponse(TypedDict):
    items: NotRequired["aws_sdk_mgn.types.import_list.ImportList"]
    """<p>List import response items.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>List import response next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mgn.types.import_list

        out["items"] = aws_sdk_mgn.types.import_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportsResponse:
    out: ListImportsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_mgn.types.import_list

        out["items"] = aws_sdk_mgn.types.import_list.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
