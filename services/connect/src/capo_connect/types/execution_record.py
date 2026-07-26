"""Generated from Smithy shape ``com.amazonaws.connect#ExecutionRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.execution_record_status
    import capo_connect.types.execution_record_string
    import capo_connect.types.test_case_resource_id
    import capo_connect.types.timestamp


class ExecutionRecord(TypedDict, closed=True):
    observation_id: NotRequired[
        "capo_connect.types.test_case_resource_id.TestCaseResourceId"
    ]
    """<p>The identifier of the execution record.</p>"""
    status: NotRequired[
        "capo_connect.types.execution_record_status.ExecutionRecordStatus"
    ]
    """<p>The status of the action execution.</p>"""
    timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the action was executed.</p>"""
    record: NotRequired[
        "capo_connect.types.execution_record_string.ExecutionRecordString"
    ]
    """<p>The details of the executed record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionRecord) -> dict:
    out: dict = {}
    if "observation_id" in value:
        out["ObservationId"] = value["observation_id"]
    if "status" in value:
        import capo_connect.types.execution_record_status

        out["Status"] = capo_connect.types.execution_record_status.serialize_json(
            value["status"]
        )
    if "timestamp" in value:
        import capo_connect.types.timestamp

        out["Timestamp"] = capo_connect.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "record" in value:
        out["Record"] = value["record"]
    return out


def deserialize_json(data: dict) -> ExecutionRecord:
    out: ExecutionRecord = {}  # type: ignore[typeddict-item]
    if "ObservationId" in data:
        out["observation_id"] = data["ObservationId"]
    if "Status" in data:
        import capo_connect.types.execution_record_status

        out["status"] = capo_connect.types.execution_record_status.deserialize_json(
            data["Status"]
        )
    if "Timestamp" in data:
        import capo_connect.types.timestamp

        out["timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    if "Record" in data:
        out["record"] = data["Record"]
    return out
