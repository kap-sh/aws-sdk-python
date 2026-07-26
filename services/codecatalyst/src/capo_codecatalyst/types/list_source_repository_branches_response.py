"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListSourceRepositoryBranchesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.list_source_repository_branches_items


class ListSourceRepositoryBranchesResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""
    items: "capo_codecatalyst.types.list_source_repository_branches_items.ListSourceRepositoryBranchesItems"
    """<p>Information about the source branches.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceRepositoryBranchesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_codecatalyst.types.list_source_repository_branches_items

    out["items"] = (
        capo_codecatalyst.types.list_source_repository_branches_items.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListSourceRepositoryBranchesResponse:
    out: ListSourceRepositoryBranchesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import capo_codecatalyst.types.list_source_repository_branches_items

        out["items"] = (
            capo_codecatalyst.types.list_source_repository_branches_items.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError(
            "ListSourceRepositoryBranchesResponse.items required"
        )
    return out
