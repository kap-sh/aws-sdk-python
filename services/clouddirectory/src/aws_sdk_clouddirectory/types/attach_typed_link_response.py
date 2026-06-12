"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttachTypedLinkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.typed_link_specifier


class AttachTypedLinkResponse(TypedDict):
    typed_link_specifier: NotRequired[
        "aws_sdk_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier"
    ]
    """<p>Returns a typed link specifier as output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachTypedLinkResponse) -> dict:
    out: dict = {}
    if "typed_link_specifier" in value:
        import aws_sdk_clouddirectory.types.typed_link_specifier

        out["TypedLinkSpecifier"] = (
            aws_sdk_clouddirectory.types.typed_link_specifier.serialize_json(
                value["typed_link_specifier"]
            )
        )
    return out


def deserialize_json(data: dict) -> AttachTypedLinkResponse:
    out: AttachTypedLinkResponse = {}  # type: ignore[typeddict-item]
    if "TypedLinkSpecifier" in data:
        import aws_sdk_clouddirectory.types.typed_link_specifier

        out["typed_link_specifier"] = (
            aws_sdk_clouddirectory.types.typed_link_specifier.deserialize_json(
                data["TypedLinkSpecifier"]
            )
        )
    return out
