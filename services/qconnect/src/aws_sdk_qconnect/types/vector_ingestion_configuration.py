"""Generated from Smithy shape ``com.amazonaws.qconnect#VectorIngestionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.chunking_configuration
    import aws_sdk_qconnect.types.parsing_configuration


class VectorIngestionConfiguration(TypedDict):
    chunking_configuration: NotRequired[
        "aws_sdk_qconnect.types.chunking_configuration.ChunkingConfiguration"
    ]
    """<p>Details about how to chunk the documents in the data source. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.</p>"""
    parsing_configuration: NotRequired[
        "aws_sdk_qconnect.types.parsing_configuration.ParsingConfiguration"
    ]
    """<p>A custom parser for data source documents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorIngestionConfiguration) -> dict:
    out: dict = {}
    if "chunking_configuration" in value:
        import aws_sdk_qconnect.types.chunking_configuration

        out["chunkingConfiguration"] = (
            aws_sdk_qconnect.types.chunking_configuration.serialize_json(
                value["chunking_configuration"]
            )
        )
    if "parsing_configuration" in value:
        import aws_sdk_qconnect.types.parsing_configuration

        out["parsingConfiguration"] = (
            aws_sdk_qconnect.types.parsing_configuration.serialize_json(
                value["parsing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorIngestionConfiguration:
    out: VectorIngestionConfiguration = {}  # type: ignore[typeddict-item]
    if "chunkingConfiguration" in data:
        import aws_sdk_qconnect.types.chunking_configuration

        out["chunking_configuration"] = (
            aws_sdk_qconnect.types.chunking_configuration.deserialize_json(
                data["chunkingConfiguration"]
            )
        )
    if "parsingConfiguration" in data:
        import aws_sdk_qconnect.types.parsing_configuration

        out["parsing_configuration"] = (
            aws_sdk_qconnect.types.parsing_configuration.deserialize_json(
                data["parsingConfiguration"]
            )
        )
    return out
