"""Generated from Smithy shape ``com.amazonaws.pipes#BatchArrayProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.batch_array_size


class BatchArrayProperties(TypedDict, closed=True):
    size: NotRequired["aws_sdk_pipes.types.batch_array_size.BatchArraySize"]
    """<p>The size of the array, if this is an array batch job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchArrayProperties) -> dict:
    out: dict = {}
    if "size" in value:
        out["Size"] = value["size"]
    return out


def deserialize_json(data: dict) -> BatchArrayProperties:
    out: BatchArrayProperties = {}  # type: ignore[typeddict-item]
    if "Size" in data:
        out["size"] = data["Size"]
    return out
