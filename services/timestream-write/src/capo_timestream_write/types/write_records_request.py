"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#WriteRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_write.types.record
    import capo_timestream_write.types.records
    import capo_timestream_write.types.resource_name


class WriteRecordsRequest(TypedDict, closed=True):
    database_name: "capo_timestream_write.types.resource_name.ResourceName"
    """<p>The name of the Timestream database.</p>"""
    table_name: "capo_timestream_write.types.resource_name.ResourceName"
    """<p>The name of the Timestream table.</p>"""
    common_attributes: NotRequired["capo_timestream_write.types.record.Record"]
    """<p>A record that contains the common measure, dimension, time, and version attributes shared across all the records in the request. The measure and dimension attributes specified will be merged with the measure and dimension attributes in the records object when the data is written into Timestream. Dimensions may not overlap, or a <code>ValidationException</code> will be thrown. In other words, a record must contain dimensions with unique names. </p>"""
    records: "capo_timestream_write.types.records.Records"
    """<p>An array of records that contain the unique measure, dimension, time, and version attributes for each time-series data point. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WriteRecordsRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "common_attributes" in value:
        import capo_timestream_write.types.record

        out["CommonAttributes"] = (
            capo_timestream_write.types.record.serialize_aws_json_1_0(
                value["common_attributes"]
            )
        )
    import capo_timestream_write.types.records

    out["Records"] = capo_timestream_write.types.records.serialize_aws_json_1_0(
        value["records"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> WriteRecordsRequest:
    out: WriteRecordsRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("WriteRecordsRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("WriteRecordsRequest.table_name required")
    if "CommonAttributes" in data:
        import capo_timestream_write.types.record

        out["common_attributes"] = (
            capo_timestream_write.types.record.deserialize_aws_json_1_0(
                data["CommonAttributes"]
            )
        )
    if "Records" in data:
        import capo_timestream_write.types.records

        out["records"] = capo_timestream_write.types.records.deserialize_aws_json_1_0(
            data["Records"]
        )
    else:
        raise DeserializationError("WriteRecordsRequest.records required")
    return out
