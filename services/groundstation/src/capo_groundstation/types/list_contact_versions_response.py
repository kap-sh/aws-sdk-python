"""Generated from Smithy shape ``com.amazonaws.groundstation#ListContactVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.contact_versions_list
    import capo_groundstation.types.pagination_token


class ListContactVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token to be used in a subsequent <code>ListContactVersions</code> call to retrieve the next page of results.</p>"""
    contact_versions_list: NotRequired[
        "capo_groundstation.types.contact_versions_list.ContactVersionsList"
    ]
    """<p>List of contact versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "contact_versions_list" in value:
        import capo_groundstation.types.contact_versions_list

        out["contactVersionsList"] = (
            capo_groundstation.types.contact_versions_list.serialize_json(
                value["contact_versions_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListContactVersionsResponse:
    out: ListContactVersionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "contactVersionsList" in data:
        import capo_groundstation.types.contact_versions_list

        out["contact_versions_list"] = (
            capo_groundstation.types.contact_versions_list.deserialize_json(
                data["contactVersionsList"]
            )
        )
    return out
