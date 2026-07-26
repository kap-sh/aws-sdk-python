"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListIncomingTypedLinksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.typed_link_specifier_list


class ListIncomingTypedLinksResponse(TypedDict, closed=True):
    link_specifiers: NotRequired[
        "capo_clouddirectory.types.typed_link_specifier_list.TypedLinkSpecifierList"
    ]
    """<p>Returns one or more typed link specifiers as output.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIncomingTypedLinksResponse) -> dict:
    out: dict = {}
    if "link_specifiers" in value:
        import capo_clouddirectory.types.typed_link_specifier_list

        out["LinkSpecifiers"] = (
            capo_clouddirectory.types.typed_link_specifier_list.serialize_json(
                value["link_specifiers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIncomingTypedLinksResponse:
    out: ListIncomingTypedLinksResponse = {}  # type: ignore[typeddict-item]
    if "LinkSpecifiers" in data:
        import capo_clouddirectory.types.typed_link_specifier_list

        out["link_specifiers"] = (
            capo_clouddirectory.types.typed_link_specifier_list.deserialize_json(
                data["LinkSpecifiers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
