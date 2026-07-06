"""Generated from Smithy shape ``com.amazonaws.batch#EphemeralStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer


class EphemeralStorage(TypedDict, closed=True):
    size_in_gi_b: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is <code>21</code> GiB and the maximum supported value is <code>200</code> GiB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemeralStorage) -> dict:
    out: dict = {}
    if "size_in_gi_b" in value:
        out["sizeInGiB"] = value["size_in_gi_b"]
    return out


def deserialize_json(data: dict) -> EphemeralStorage:
    out: EphemeralStorage = {}  # type: ignore[typeddict-item]
    if "sizeInGiB" in data:
        out["size_in_gi_b"] = data["sizeInGiB"]
    return out
