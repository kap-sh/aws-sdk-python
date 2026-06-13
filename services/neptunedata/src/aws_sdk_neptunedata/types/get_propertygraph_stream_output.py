"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetPropertygraphStreamOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.propertygraph_records_list
    import aws_sdk_neptunedata.types.string_valued_map


class GetPropertygraphStreamOutput(TypedDict):
    last_event_id: "aws_sdk_neptunedata.types.string_valued_map.StringValuedMap"
    """<p>Sequence identifier of the last change in the stream response.</p> <p>An event ID is composed of two fields: a <code>commitNum</code>, which identifies a transaction that changed the graph, and an <code>opNum</code>, which identifies a specific operation within that transaction:</p>"""
    last_trx_timestamp_in_millis: "int"
    """<p>The time at which the commit for the transaction was requested, in milliseconds from the Unix epoch.</p>"""
    format: "str"
    """<p>Serialization format for the change records being returned. Currently, the only supported value is <code>PG_JSON</code>.</p>"""
    records: (
        "aws_sdk_neptunedata.types.propertygraph_records_list.PropertygraphRecordsList"
    )
    """<p>An array of serialized change-log stream records included in the response.</p>"""
    total_records: "int"
    """<p>The total number of records in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPropertygraphStreamOutput) -> dict:
    out: dict = {}
    import aws_sdk_neptunedata.types.string_valued_map

    out["lastEventId"] = aws_sdk_neptunedata.types.string_valued_map.serialize_json(
        value["last_event_id"]
    )
    out["lastTrxTimestamp"] = value["last_trx_timestamp_in_millis"]
    out["format"] = value["format"]
    import aws_sdk_neptunedata.types.propertygraph_records_list

    out["records"] = (
        aws_sdk_neptunedata.types.propertygraph_records_list.serialize_json(
            value["records"]
        )
    )
    out["totalRecords"] = value["total_records"]
    return out


def deserialize_json(data: dict) -> GetPropertygraphStreamOutput:
    out: GetPropertygraphStreamOutput = {}  # type: ignore[typeddict-item]
    if "lastEventId" in data:
        import aws_sdk_neptunedata.types.string_valued_map

        out["last_event_id"] = (
            aws_sdk_neptunedata.types.string_valued_map.deserialize_json(
                data["lastEventId"]
            )
        )
    else:
        raise DeserializationError(
            "GetPropertygraphStreamOutput.last_event_id required"
        )
    if "lastTrxTimestamp" in data:
        out["last_trx_timestamp_in_millis"] = data["lastTrxTimestamp"]
    else:
        raise DeserializationError(
            "GetPropertygraphStreamOutput.last_trx_timestamp_in_millis required"
        )
    if "format" in data:
        out["format"] = data["format"]
    else:
        raise DeserializationError("GetPropertygraphStreamOutput.format required")
    if "records" in data:
        import aws_sdk_neptunedata.types.propertygraph_records_list

        out["records"] = (
            aws_sdk_neptunedata.types.propertygraph_records_list.deserialize_json(
                data["records"]
            )
        )
    else:
        raise DeserializationError("GetPropertygraphStreamOutput.records required")
    if "totalRecords" in data:
        out["total_records"] = data["totalRecords"]
    else:
        raise DeserializationError(
            "GetPropertygraphStreamOutput.total_records required"
        )
    return out
