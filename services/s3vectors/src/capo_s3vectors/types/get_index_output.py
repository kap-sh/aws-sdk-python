"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetIndexOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.index


class GetIndexOutput(TypedDict, closed=True):
    index: "capo_s3vectors.types.index.Index"
    """<p>The attributes of the vector index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexOutput) -> dict:
    out: dict = {}
    import capo_s3vectors.types.index

    out["index"] = capo_s3vectors.types.index.serialize_json(value["index"])
    return out


def deserialize_json(data: dict) -> GetIndexOutput:
    out: GetIndexOutput = {}  # type: ignore[typeddict-item]
    if "index" in data:
        import capo_s3vectors.types.index

        out["index"] = capo_s3vectors.types.index.deserialize_json(data["index"])
    else:
        raise DeserializationError("GetIndexOutput.index required")
    return out
