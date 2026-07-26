"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchListObjectParentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.object_identifier_and_link_name_list


class BatchListObjectParentsResponse(TypedDict, closed=True):
    parent_links: NotRequired[
        "capo_clouddirectory.types.object_identifier_and_link_name_list.ObjectIdentifierAndLinkNameList"
    ]
    """<p>Returns a list of parent reference and LinkName Tuples.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchListObjectParentsResponse) -> dict:
    out: dict = {}
    if "parent_links" in value:
        import capo_clouddirectory.types.object_identifier_and_link_name_list

        out["ParentLinks"] = (
            capo_clouddirectory.types.object_identifier_and_link_name_list.serialize_json(
                value["parent_links"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchListObjectParentsResponse:
    out: BatchListObjectParentsResponse = {}  # type: ignore[typeddict-item]
    if "ParentLinks" in data:
        import capo_clouddirectory.types.object_identifier_and_link_name_list

        out["parent_links"] = (
            capo_clouddirectory.types.object_identifier_and_link_name_list.deserialize_json(
                data["ParentLinks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
