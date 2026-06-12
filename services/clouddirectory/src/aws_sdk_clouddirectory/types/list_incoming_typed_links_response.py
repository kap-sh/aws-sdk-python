"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListIncomingTypedLinksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.typed_link_specifier_list


class ListIncomingTypedLinksResponse(TypedDict):
    link_specifiers: NotRequired[
        "aws_sdk_clouddirectory.types.typed_link_specifier_list.TypedLinkSpecifierList"
    ]
    """<p>Returns one or more typed link specifiers as output.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIncomingTypedLinksResponse) -> dict:
    out: dict = {}
    if "link_specifiers" in value:
        import aws_sdk_clouddirectory.types.typed_link_specifier_list

        out["LinkSpecifiers"] = (
            aws_sdk_clouddirectory.types.typed_link_specifier_list.serialize_json(
                value["link_specifiers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIncomingTypedLinksResponse:
    out: ListIncomingTypedLinksResponse = {}  # type: ignore[typeddict-item]
    if "LinkSpecifiers" in data:
        import aws_sdk_clouddirectory.types.typed_link_specifier_list

        out["link_specifiers"] = (
            aws_sdk_clouddirectory.types.typed_link_specifier_list.deserialize_json(
                data["LinkSpecifiers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
