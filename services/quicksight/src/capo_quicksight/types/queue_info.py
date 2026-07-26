"""Generated from Smithy shape ``com.amazonaws.quicksight#QueueInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.string


class QueueInfo(TypedDict, closed=True):
    waiting_on_ingestion: "capo_quicksight.types.string.String"
    """<p>The ID of the queued ingestion.</p>"""
    queued_ingestion: "capo_quicksight.types.string.String"
    """<p>The ID of the ongoing ingestion. The queued ingestion is waiting for the ongoing ingestion to complete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueInfo) -> dict:
    out: dict = {}
    out["WaitingOnIngestion"] = value["waiting_on_ingestion"]
    out["QueuedIngestion"] = value["queued_ingestion"]
    return out


def deserialize_json(data: dict) -> QueueInfo:
    out: QueueInfo = {}  # type: ignore[typeddict-item]
    if "WaitingOnIngestion" in data:
        out["waiting_on_ingestion"] = data["WaitingOnIngestion"]
    else:
        raise DeserializationError("QueueInfo.waiting_on_ingestion required")
    if "QueuedIngestion" in data:
        out["queued_ingestion"] = data["QueuedIngestion"]
    else:
        raise DeserializationError("QueueInfo.queued_ingestion required")
    return out
