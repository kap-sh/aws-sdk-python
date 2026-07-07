"""Generated from Smithy shape ``com.amazonaws.neptunedata#PropertygraphRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.propertygraph_data
    import aws_sdk_neptunedata.types.string_valued_map


class PropertygraphRecord(TypedDict, closed=True):
    commit_timestamp_in_millis: "int"
    """<p>The time at which the commit for the transaction was requested, in milliseconds from the Unix epoch.</p>"""
    event_id: "aws_sdk_neptunedata.types.string_valued_map.StringValuedMap"
    """<p>The sequence identifier of the stream change record.</p>"""
    data: "aws_sdk_neptunedata.types.propertygraph_data.PropertygraphData"
    """<p>The serialized Gremlin or openCypher change record.</p>"""
    op: "str"
    """<p>The operation that created the change.</p>"""
    is_last_op: NotRequired["bool"]
    """<p>Only present if this operation is the last one in its transaction. If present, it is set to true. It is useful for ensuring that an entire transaction is consumed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertygraphRecord) -> dict:
    out: dict = {}
    out["commitTimestamp"] = value["commit_timestamp_in_millis"]
    import aws_sdk_neptunedata.types.string_valued_map

    out["eventId"] = aws_sdk_neptunedata.types.string_valued_map.serialize_json(
        value["event_id"]
    )
    import aws_sdk_neptunedata.types.propertygraph_data

    out["data"] = aws_sdk_neptunedata.types.propertygraph_data.serialize_json(
        value["data"]
    )
    out["op"] = value["op"]
    if "is_last_op" in value:
        out["isLastOp"] = value["is_last_op"]
    return out


def deserialize_json(data: dict) -> PropertygraphRecord:
    out: PropertygraphRecord = {}  # type: ignore[typeddict-item]
    if "commitTimestamp" in data:
        out["commit_timestamp_in_millis"] = data["commitTimestamp"]
    else:
        raise DeserializationError(
            "PropertygraphRecord.commit_timestamp_in_millis required"
        )
    if "eventId" in data:
        import aws_sdk_neptunedata.types.string_valued_map

        out["event_id"] = aws_sdk_neptunedata.types.string_valued_map.deserialize_json(
            data["eventId"]
        )
    else:
        raise DeserializationError("PropertygraphRecord.event_id required")
    if "data" in data:
        import aws_sdk_neptunedata.types.propertygraph_data

        out["data"] = aws_sdk_neptunedata.types.propertygraph_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("PropertygraphRecord.data required")
    if "op" in data:
        out["op"] = data["op"]
    else:
        raise DeserializationError("PropertygraphRecord.op required")
    if "isLastOp" in data:
        out["is_last_op"] = data["isLastOp"]
    return out
