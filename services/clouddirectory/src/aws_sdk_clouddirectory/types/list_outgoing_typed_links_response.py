"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListOutgoingTypedLinksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.typed_link_specifier_list


class ListOutgoingTypedLinksResponse(TypedDict, closed=True):
    typed_link_specifiers: NotRequired[
        "aws_sdk_clouddirectory.types.typed_link_specifier_list.TypedLinkSpecifierList"
    ]
    """<p>Returns a typed link specifier as output.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOutgoingTypedLinksResponse) -> dict:
    out: dict = {}
    if "typed_link_specifiers" in value:
        import aws_sdk_clouddirectory.types.typed_link_specifier_list

        out["TypedLinkSpecifiers"] = (
            aws_sdk_clouddirectory.types.typed_link_specifier_list.serialize_json(
                value["typed_link_specifiers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOutgoingTypedLinksResponse:
    out: ListOutgoingTypedLinksResponse = {}  # type: ignore[typeddict-item]
    if "TypedLinkSpecifiers" in data:
        import aws_sdk_clouddirectory.types.typed_link_specifier_list

        out["typed_link_specifiers"] = (
            aws_sdk_clouddirectory.types.typed_link_specifier_list.deserialize_json(
                data["TypedLinkSpecifiers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
