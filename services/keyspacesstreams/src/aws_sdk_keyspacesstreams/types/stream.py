"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#Stream``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_keyspacesstreams.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.keyspace_name
    import aws_sdk_keyspacesstreams.types.stream_arn
    import aws_sdk_keyspacesstreams.types.table_name


class Stream(TypedDict):
    stream_arn: "aws_sdk_keyspacesstreams.types.stream_arn.StreamArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies this stream.</p>"""
    keyspace_name: "aws_sdk_keyspacesstreams.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace containing the table associated with this stream.</p>"""
    table_name: "aws_sdk_keyspacesstreams.types.table_name.TableName"
    """<p>The name of the table associated with this stream.</p>"""
    stream_label: "str"
    """<p>A unique identifier for this stream that can be used in stream operations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Stream) -> dict:
    out: dict = {}
    out["streamArn"] = value["stream_arn"]
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    out["streamLabel"] = value["stream_label"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Stream:
    out: Stream = {}  # type: ignore[typeddict-item]
    if "streamArn" in data:
        out["stream_arn"] = data["streamArn"]
    else:
        raise DeserializationError("Stream.stream_arn required")
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("Stream.keyspace_name required")
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("Stream.table_name required")
    if "streamLabel" in data:
        out["stream_label"] = data["streamLabel"]
    else:
        raise DeserializationError("Stream.stream_label required")
    return out
