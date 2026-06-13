"""Generated from Smithy shape ``com.amazonaws.neptunegraph#VectorSearchConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.vector_search_dimension


class VectorSearchConfiguration(TypedDict):
    dimension: (
        "aws_sdk_neptune_graph.types.vector_search_dimension.VectorSearchDimension"
    )
    """<p>The number of dimensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchConfiguration) -> dict:
    out: dict = {}
    out["dimension"] = value["dimension"]
    return out


def deserialize_json(data: dict) -> VectorSearchConfiguration:
    out: VectorSearchConfiguration = {}  # type: ignore[typeddict-item]
    if "dimension" in data:
        out["dimension"] = data["dimension"]
    else:
        raise DeserializationError("VectorSearchConfiguration.dimension required")
    return out
