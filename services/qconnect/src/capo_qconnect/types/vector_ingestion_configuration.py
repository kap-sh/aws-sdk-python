"""Generated from Smithy shape ``com.amazonaws.qconnect#VectorIngestionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.chunking_configuration
    import capo_qconnect.types.parsing_configuration


class VectorIngestionConfiguration(TypedDict, closed=True):
    chunking_configuration: NotRequired[
        "capo_qconnect.types.chunking_configuration.ChunkingConfiguration"
    ]
    """<p>Details about how to chunk the documents in the data source. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.</p>"""
    parsing_configuration: NotRequired[
        "capo_qconnect.types.parsing_configuration.ParsingConfiguration"
    ]
    """<p>A custom parser for data source documents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorIngestionConfiguration) -> dict:
    out: dict = {}
    if "chunking_configuration" in value:
        import capo_qconnect.types.chunking_configuration

        out["chunkingConfiguration"] = (
            capo_qconnect.types.chunking_configuration.serialize_json(
                value["chunking_configuration"]
            )
        )
    if "parsing_configuration" in value:
        import capo_qconnect.types.parsing_configuration

        out["parsingConfiguration"] = (
            capo_qconnect.types.parsing_configuration.serialize_json(
                value["parsing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorIngestionConfiguration:
    out: VectorIngestionConfiguration = {}  # type: ignore[typeddict-item]
    if "chunkingConfiguration" in data:
        import capo_qconnect.types.chunking_configuration

        out["chunking_configuration"] = (
            capo_qconnect.types.chunking_configuration.deserialize_json(
                data["chunkingConfiguration"]
            )
        )
    if "parsingConfiguration" in data:
        import capo_qconnect.types.parsing_configuration

        out["parsing_configuration"] = (
            capo_qconnect.types.parsing_configuration.deserialize_json(
                data["parsingConfiguration"]
            )
        )
    return out
