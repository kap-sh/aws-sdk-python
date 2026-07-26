"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListObjectChildrenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.link_name_to_object_identifier_map
    import capo_clouddirectory.types.next_token


class ListObjectChildrenResponse(TypedDict, closed=True):
    children: NotRequired[
        "capo_clouddirectory.types.link_name_to_object_identifier_map.LinkNameToObjectIdentifierMap"
    ]
    """<p>Children structure, which is a map with key as the <code>LinkName</code> and <code>ObjectIdentifier</code> as the value.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectChildrenResponse) -> dict:
    out: dict = {}
    if "children" in value:
        import capo_clouddirectory.types.link_name_to_object_identifier_map

        out["Children"] = (
            capo_clouddirectory.types.link_name_to_object_identifier_map.serialize_json(
                value["children"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListObjectChildrenResponse:
    out: ListObjectChildrenResponse = {}  # type: ignore[typeddict-item]
    if "Children" in data:
        import capo_clouddirectory.types.link_name_to_object_identifier_map

        out["children"] = (
            capo_clouddirectory.types.link_name_to_object_identifier_map.deserialize_json(
                data["Children"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
