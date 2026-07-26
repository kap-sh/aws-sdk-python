"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListObjectParentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.object_identifier_and_link_name_list
    import capo_clouddirectory.types.object_identifier_to_link_name_map


class ListObjectParentsResponse(TypedDict, closed=True):
    parents: NotRequired[
        "capo_clouddirectory.types.object_identifier_to_link_name_map.ObjectIdentifierToLinkNameMap"
    ]
    """<p>The parent structure, which is a map with key as the <code>ObjectIdentifier</code> and LinkName as the value.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    parent_links: NotRequired[
        "capo_clouddirectory.types.object_identifier_and_link_name_list.ObjectIdentifierAndLinkNameList"
    ]
    """<p>Returns a list of parent reference and LinkName Tuples.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectParentsResponse) -> dict:
    out: dict = {}
    if "parents" in value:
        import capo_clouddirectory.types.object_identifier_to_link_name_map

        out["Parents"] = (
            capo_clouddirectory.types.object_identifier_to_link_name_map.serialize_json(
                value["parents"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "parent_links" in value:
        import capo_clouddirectory.types.object_identifier_and_link_name_list

        out["ParentLinks"] = (
            capo_clouddirectory.types.object_identifier_and_link_name_list.serialize_json(
                value["parent_links"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListObjectParentsResponse:
    out: ListObjectParentsResponse = {}  # type: ignore[typeddict-item]
    if "Parents" in data:
        import capo_clouddirectory.types.object_identifier_to_link_name_map

        out["parents"] = (
            capo_clouddirectory.types.object_identifier_to_link_name_map.deserialize_json(
                data["Parents"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ParentLinks" in data:
        import capo_clouddirectory.types.object_identifier_and_link_name_list

        out["parent_links"] = (
            capo_clouddirectory.types.object_identifier_and_link_name_list.deserialize_json(
                data["ParentLinks"]
            )
        )
    return out
