"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationStateInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class ReplicationStateInfo(TypedDict, closed=True):
    code: NotRequired["capo_kafka.types.__string.__string"]
    """Code that describes the current state of the replicator."""
    message: NotRequired["capo_kafka.types.__string.__string"]
    """Message that describes the state of the replicator."""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStateInfo) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ReplicationStateInfo:
    out: ReplicationStateInfo = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
