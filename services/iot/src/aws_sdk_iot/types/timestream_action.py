"""Generated from Smithy shape ``com.amazonaws.iot#TimestreamAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.timestream_database_name
    import aws_sdk_iot.types.timestream_dimension_list
    import aws_sdk_iot.types.timestream_table_name
    import aws_sdk_iot.types.timestream_timestamp


class TimestreamAction(TypedDict):
    role_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the role that grants permission to write to the Amazon Timestream database table.</p>"""
    database_name: "aws_sdk_iot.types.timestream_database_name.TimestreamDatabaseName"
    """<p>The name of an Amazon Timestream database.</p>"""
    table_name: "aws_sdk_iot.types.timestream_table_name.TimestreamTableName"
    """<p>The name of the database table into which to write the measure records.</p>"""
    dimensions: "aws_sdk_iot.types.timestream_dimension_list.TimestreamDimensionList"
    """<p>Metadata attributes of the time series that are written in each measure record.</p>"""
    timestamp: NotRequired["aws_sdk_iot.types.timestream_timestamp.TimestreamTimestamp"]
    """<p>Specifies an application-defined value to replace the default value assigned to the Timestream record's timestamp in the <code>time</code> column.</p> <p>You can use this property to specify the value and the precision of the Timestream record's timestamp. You can specify a value from the message payload or a value computed by a substitution template.</p> <p>If omitted, the topic rule action assigns the timestamp, in milliseconds, at the time it processed the rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestreamAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["databaseName"] = value["database_name"]
    out["tableName"] = value["table_name"]
    import aws_sdk_iot.types.timestream_dimension_list

    out["dimensions"] = aws_sdk_iot.types.timestream_dimension_list.serialize_json(
        value["dimensions"]
    )
    if "timestamp" in value:
        import aws_sdk_iot.types.timestream_timestamp

        out["timestamp"] = aws_sdk_iot.types.timestream_timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> TimestreamAction:
    out: TimestreamAction = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("TimestreamAction.role_arn required")
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("TimestreamAction.database_name required")
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("TimestreamAction.table_name required")
    if "dimensions" in data:
        import aws_sdk_iot.types.timestream_dimension_list

        out["dimensions"] = (
            aws_sdk_iot.types.timestream_dimension_list.deserialize_json(
                data["dimensions"]
            )
        )
    else:
        raise DeserializationError("TimestreamAction.dimensions required")
    if "timestamp" in data:
        import aws_sdk_iot.types.timestream_timestamp

        out["timestamp"] = aws_sdk_iot.types.timestream_timestamp.deserialize_json(
            data["timestamp"]
        )
    return out
