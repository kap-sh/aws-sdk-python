"""Generated from Smithy shape ``com.amazonaws.qconnect#SourceContentDataDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.citation_span
    import capo_qconnect.types.ranking_data
    import capo_qconnect.types.source_content_type
    import capo_qconnect.types.text_data
    import capo_qconnect.types.uuid


class SourceContentDataDetails(TypedDict, closed=True):
    id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the source content.</p>"""
    type: "capo_qconnect.types.source_content_type.SourceContentType"
    """<p>The type of the source content.</p>"""
    text_data: "capo_qconnect.types.text_data.TextData"
    """<p> Details about the source content text data.</p>"""
    ranking_data: "capo_qconnect.types.ranking_data.RankingData"
    """<p>Details about the source content ranking data.</p>"""
    citation_span: NotRequired["capo_qconnect.types.citation_span.CitationSpan"]
    """<p>Contains information about where the text with a citation begins and ends in the generated output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceContentDataDetails) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["type"] = value["type"]
    import capo_qconnect.types.text_data

    out["textData"] = capo_qconnect.types.text_data.serialize_json(value["text_data"])
    import capo_qconnect.types.ranking_data

    out["rankingData"] = capo_qconnect.types.ranking_data.serialize_json(
        value["ranking_data"]
    )
    if "citation_span" in value:
        import capo_qconnect.types.citation_span

        out["citationSpan"] = capo_qconnect.types.citation_span.serialize_json(
            value["citation_span"]
        )
    return out


def deserialize_json(data: dict) -> SourceContentDataDetails:
    out: SourceContentDataDetails = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SourceContentDataDetails.id required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SourceContentDataDetails.type required")
    if "textData" in data:
        import capo_qconnect.types.text_data

        out["text_data"] = capo_qconnect.types.text_data.deserialize_json(
            data["textData"]
        )
    else:
        raise DeserializationError("SourceContentDataDetails.text_data required")
    if "rankingData" in data:
        import capo_qconnect.types.ranking_data

        out["ranking_data"] = capo_qconnect.types.ranking_data.deserialize_json(
            data["rankingData"]
        )
    else:
        raise DeserializationError("SourceContentDataDetails.ranking_data required")
    if "citationSpan" in data:
        import capo_qconnect.types.citation_span

        out["citation_span"] = capo_qconnect.types.citation_span.deserialize_json(
            data["citationSpan"]
        )
    return out
