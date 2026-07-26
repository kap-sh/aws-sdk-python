"""Generated from Smithy shape ``com.amazonaws.s3vectors#PutInputVector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.vector_data
    import capo_s3vectors.types.vector_key
    import capo_s3vectors.types.vector_metadata


class PutInputVector(TypedDict, closed=True):
    key: "capo_s3vectors.types.vector_key.VectorKey"
    """<p>The name of the vector. The key uniquely identifies the vector in a vector index. </p>"""
    data: "capo_s3vectors.types.vector_data.VectorData"
    """<p>The vector data of the vector. </p> <p>Vector dimensions must match the dimension count that's configured for the vector index.</p> <ul> <li> <p>For the <code>cosine</code> distance metric, zero vectors (vectors containing all zeros) aren't allowed.</p> </li> <li> <p>For both <code>cosine</code> and <code>euclidean</code> distance metrics, vector data must contain only valid floating-point values. Invalid values such as NaN (Not a Number) or Infinity aren't allowed.</p> </li> </ul>"""
    metadata: "capo_s3vectors.types.vector_metadata.VectorMetadata"
    """<p>Metadata about the vector. All metadata entries undergo validation to ensure they meet the format requirements for size and data types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutInputVector) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_s3vectors.types.vector_data

    out["data"] = capo_s3vectors.types.vector_data.serialize_json(value["data"])
    out["metadata"] = value.get("metadata", {})
    return out


def deserialize_json(data: dict) -> PutInputVector:
    out: PutInputVector = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("PutInputVector.key required")
    if "data" in data:
        import capo_s3vectors.types.vector_data

        out["data"] = capo_s3vectors.types.vector_data.deserialize_json(data["data"])
    else:
        raise DeserializationError("PutInputVector.data required")
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    else:
        out["metadata"] = {}
    return out
