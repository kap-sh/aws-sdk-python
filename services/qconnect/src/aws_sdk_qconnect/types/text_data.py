"""Generated from Smithy shape ``com.amazonaws.qconnect#TextData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.document_text


class TextData(TypedDict, closed=True):
    title: NotRequired["aws_sdk_qconnect.types.document_text.DocumentText"]
    excerpt: NotRequired["aws_sdk_qconnect.types.document_text.DocumentText"]


# --- restJson1 ser/de ---
def serialize_json(value: TextData) -> dict:
    out: dict = {}
    if "title" in value:
        import aws_sdk_qconnect.types.document_text

        out["title"] = aws_sdk_qconnect.types.document_text.serialize_json(
            value["title"]
        )
    if "excerpt" in value:
        import aws_sdk_qconnect.types.document_text

        out["excerpt"] = aws_sdk_qconnect.types.document_text.serialize_json(
            value["excerpt"]
        )
    return out


def deserialize_json(data: dict) -> TextData:
    out: TextData = {}  # type: ignore[typeddict-item]
    if "title" in data:
        import aws_sdk_qconnect.types.document_text

        out["title"] = aws_sdk_qconnect.types.document_text.deserialize_json(
            data["title"]
        )
    if "excerpt" in data:
        import aws_sdk_qconnect.types.document_text

        out["excerpt"] = aws_sdk_qconnect.types.document_text.deserialize_json(
            data["excerpt"]
        )
    return out
