"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListChangesetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.changeset_list
    import aws_sdk_finspace_data.types.pagination_token


class ListChangesetsResponse(TypedDict):
    changesets: NotRequired["aws_sdk_finspace_data.types.changeset_list.ChangesetList"]
    """<p>List of Changesets found.</p>"""
    next_token: NotRequired[
        "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
    ]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChangesetsResponse) -> dict:
    out: dict = {}
    if "changesets" in value:
        import aws_sdk_finspace_data.types.changeset_list

        out["changesets"] = aws_sdk_finspace_data.types.changeset_list.serialize_json(
            value["changesets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChangesetsResponse:
    out: ListChangesetsResponse = {}  # type: ignore[typeddict-item]
    if "changesets" in data:
        import aws_sdk_finspace_data.types.changeset_list

        out["changesets"] = aws_sdk_finspace_data.types.changeset_list.deserialize_json(
            data["changesets"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
