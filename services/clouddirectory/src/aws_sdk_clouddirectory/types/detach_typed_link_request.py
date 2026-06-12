"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DetachTypedLinkRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.typed_link_specifier


class DetachTypedLinkRequest(TypedDict):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the directory where you want to detach the typed link.</p>"""
    typed_link_specifier: (
        "aws_sdk_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier"
    )
    """<p>Used to accept a typed link specifier as input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachTypedLinkRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.typed_link_specifier

    out["TypedLinkSpecifier"] = (
        aws_sdk_clouddirectory.types.typed_link_specifier.serialize_json(
            value["typed_link_specifier"]
        )
    )
    return out


def deserialize_json(data: dict) -> DetachTypedLinkRequest:
    out: DetachTypedLinkRequest = {}  # type: ignore[typeddict-item]
    if "TypedLinkSpecifier" in data:
        import aws_sdk_clouddirectory.types.typed_link_specifier

        out["typed_link_specifier"] = (
            aws_sdk_clouddirectory.types.typed_link_specifier.deserialize_json(
                data["TypedLinkSpecifier"]
            )
        )
    else:
        raise DeserializationError(
            "DetachTypedLinkRequest.typed_link_specifier required"
        )
    return out
