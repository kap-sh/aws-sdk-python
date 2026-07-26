"""Generated from Smithy shape ``com.amazonaws.batch#ArrayProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer


class ArrayProperties(TypedDict, closed=True):
    size: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The size of the array job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArrayProperties) -> dict:
    out: dict = {}
    if "size" in value:
        out["size"] = value["size"]
    return out


def deserialize_json(data: dict) -> ArrayProperties:
    out: ArrayProperties = {}  # type: ignore[typeddict-item]
    if "size" in data:
        out["size"] = data["size"]
    return out
