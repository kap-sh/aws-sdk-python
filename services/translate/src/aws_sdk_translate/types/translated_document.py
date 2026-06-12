"""Generated from Smithy shape ``com.amazonaws.translate#TranslatedDocument``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.translated_document_content


class TranslatedDocument(TypedDict):
    content: (
        "aws_sdk_translate.types.translated_document_content.TranslatedDocumentContent"
    )
    """<p>The document containing the translated content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranslatedDocument) -> dict:
    out: dict = {}
    import aws_sdk_translate.types.translated_document_content

    out["Content"] = (
        aws_sdk_translate.types.translated_document_content.serialize_aws_json_1_1(
            value["content"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TranslatedDocument:
    out: TranslatedDocument = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        import aws_sdk_translate.types.translated_document_content

        out["content"] = (
            aws_sdk_translate.types.translated_document_content.deserialize_aws_json_1_1(
                data["Content"]
            )
        )
    else:
        raise DeserializationError("TranslatedDocument.content required")
    return out
