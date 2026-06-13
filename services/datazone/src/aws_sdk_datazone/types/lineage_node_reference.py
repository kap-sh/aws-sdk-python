"""Generated from Smithy shape ``com.amazonaws.datazone#LineageNodeReference``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_node_id
    import datetime


class LineageNodeReference(TypedDict):
    id: NotRequired["aws_sdk_datazone.types.lineage_node_id.LineageNodeId"]
    """<p>The ID of the data lineage node.</p>"""
    event_timestamp: NotRequired["datetime.datetime"]
    """<p>The event timestamp of the data lineage node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageNodeReference) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "event_timestamp" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["eventTimestamp"] = (
            aws_sdk_datazone.types._prelude.timestamp.serialize_json(
                value["event_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineageNodeReference:
    out: LineageNodeReference = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "eventTimestamp" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["event_timestamp"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["eventTimestamp"]
            )
        )
    return out
