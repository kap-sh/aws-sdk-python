"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchAttachTypedLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.typed_link_specifier


class BatchAttachTypedLinkResponse(TypedDict, closed=True):
    typed_link_specifier: NotRequired[
        "aws_sdk_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier"
    ]
    """<p>Returns a typed link specifier as output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAttachTypedLinkResponse) -> dict:
    out: dict = {}
    if "typed_link_specifier" in value:
        import aws_sdk_clouddirectory.types.typed_link_specifier

        out["TypedLinkSpecifier"] = (
            aws_sdk_clouddirectory.types.typed_link_specifier.serialize_json(
                value["typed_link_specifier"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchAttachTypedLinkResponse:
    out: BatchAttachTypedLinkResponse = {}  # type: ignore[typeddict-item]
    if "TypedLinkSpecifier" in data:
        import aws_sdk_clouddirectory.types.typed_link_specifier

        out["typed_link_specifier"] = (
            aws_sdk_clouddirectory.types.typed_link_specifier.deserialize_json(
                data["TypedLinkSpecifier"]
            )
        )
    return out
