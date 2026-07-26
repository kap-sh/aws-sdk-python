"""Generated from Smithy shape ``com.amazonaws.qbusiness#IndexStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.text_document_statistics


class IndexStatistics(TypedDict, closed=True):
    text_document_statistics: NotRequired[
        "capo_qbusiness.types.text_document_statistics.TextDocumentStatistics"
    ]
    """<p>The number of documents indexed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexStatistics) -> dict:
    out: dict = {}
    if "text_document_statistics" in value:
        import capo_qbusiness.types.text_document_statistics

        out["textDocumentStatistics"] = (
            capo_qbusiness.types.text_document_statistics.serialize_json(
                value["text_document_statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> IndexStatistics:
    out: IndexStatistics = {}  # type: ignore[typeddict-item]
    if "textDocumentStatistics" in data:
        import capo_qbusiness.types.text_document_statistics

        out["text_document_statistics"] = (
            capo_qbusiness.types.text_document_statistics.deserialize_json(
                data["textDocumentStatistics"]
            )
        )
    return out
