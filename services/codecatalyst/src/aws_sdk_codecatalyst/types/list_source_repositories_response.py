"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListSourceRepositoriesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.list_source_repositories_items


class ListSourceRepositoriesResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_codecatalyst.types.list_source_repositories_items.ListSourceRepositoriesItems"
    ]
    """<p>Information about the source repositories.</p>"""
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceRepositoriesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_codecatalyst.types.list_source_repositories_items

        out["items"] = (
            aws_sdk_codecatalyst.types.list_source_repositories_items.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSourceRepositoriesResponse:
    out: ListSourceRepositoriesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_codecatalyst.types.list_source_repositories_items

        out["items"] = (
            aws_sdk_codecatalyst.types.list_source_repositories_items.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
