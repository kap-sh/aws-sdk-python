"""Generated from Smithy shape ``com.amazonaws.pipes#EcsEphemeralStorage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.ephemeral_storage_size


class EcsEphemeralStorage(TypedDict):
    size_in_gi_b: "aws_sdk_pipes.types.ephemeral_storage_size.EphemeralStorageSize"
    """<p>The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is <code>21</code> GiB and the maximum supported value is <code>200</code> GiB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsEphemeralStorage) -> dict:
    out: dict = {}
    out["sizeInGiB"] = value["size_in_gi_b"]
    return out


def deserialize_json(data: dict) -> EcsEphemeralStorage:
    out: EcsEphemeralStorage = {}  # type: ignore[typeddict-item]
    if "sizeInGiB" in data:
        out["size_in_gi_b"] = data["sizeInGiB"]
    else:
        raise DeserializationError("EcsEphemeralStorage.size_in_gi_b required")
    return out
