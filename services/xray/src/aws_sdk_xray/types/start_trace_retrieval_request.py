"""Generated from Smithy shape ``com.amazonaws.xray#StartTraceRetrievalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.timestamp
    import aws_sdk_xray.types.trace_id_list_for_retrieval


class StartTraceRetrievalRequest(TypedDict, closed=True):
    trace_ids: "aws_sdk_xray.types.trace_id_list_for_retrieval.TraceIdListForRetrieval"
    """<p> Specify the trace IDs of the traces to be retrieved. </p>"""
    start_time: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p> The start of the time range to retrieve traces. The range is inclusive, so the specified start time is included in the query. Specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC. </p>"""
    end_time: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p> The end of the time range to retrieve traces. The range is inclusive, so the specified end time is included in the query. Specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTraceRetrievalRequest) -> dict:
    out: dict = {}
    import aws_sdk_xray.types.trace_id_list_for_retrieval

    out["TraceIds"] = aws_sdk_xray.types.trace_id_list_for_retrieval.serialize_json(
        value["trace_ids"]
    )
    import aws_sdk_xray.types.timestamp

    out["StartTime"] = aws_sdk_xray.types.timestamp.serialize_json(value["start_time"])
    import aws_sdk_xray.types.timestamp

    out["EndTime"] = aws_sdk_xray.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> StartTraceRetrievalRequest:
    out: StartTraceRetrievalRequest = {}  # type: ignore[typeddict-item]
    if "TraceIds" in data:
        import aws_sdk_xray.types.trace_id_list_for_retrieval

        out["trace_ids"] = (
            aws_sdk_xray.types.trace_id_list_for_retrieval.deserialize_json(
                data["TraceIds"]
            )
        )
    else:
        raise DeserializationError("StartTraceRetrievalRequest.trace_ids required")
    if "StartTime" in data:
        import aws_sdk_xray.types.timestamp

        out["start_time"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError("StartTraceRetrievalRequest.start_time required")
    if "EndTime" in data:
        import aws_sdk_xray.types.timestamp

        out["end_time"] = aws_sdk_xray.types.timestamp.deserialize_json(data["EndTime"])
    else:
        raise DeserializationError("StartTraceRetrievalRequest.end_time required")
    return out
