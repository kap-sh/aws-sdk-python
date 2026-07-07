"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#StreamRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.attribute_map
    import aws_sdk_dynamodb_streams.types.date
    import aws_sdk_dynamodb_streams.types.positive_long_object
    import aws_sdk_dynamodb_streams.types.sequence_number
    import aws_sdk_dynamodb_streams.types.stream_view_type


class StreamRecord(TypedDict, closed=True):
    approximate_creation_date_time: NotRequired[
        "aws_sdk_dynamodb_streams.types.date.Date"
    ]
    r"""<p>The approximate date and time when the stream record was created, in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format and rounded down to the closest second.</p>"""
    keys: NotRequired["aws_sdk_dynamodb_streams.types.attribute_map.AttributeMap"]
    """<p>The primary key attribute(s) for the DynamoDB item that was modified.</p>"""
    new_image: NotRequired["aws_sdk_dynamodb_streams.types.attribute_map.AttributeMap"]
    """<p>The item in the DynamoDB table as it appeared after it was modified.</p>"""
    old_image: NotRequired["aws_sdk_dynamodb_streams.types.attribute_map.AttributeMap"]
    """<p>The item in the DynamoDB table as it appeared before it was modified.</p>"""
    sequence_number: NotRequired[
        "aws_sdk_dynamodb_streams.types.sequence_number.SequenceNumber"
    ]
    """<p>The sequence number of the stream record.</p>"""
    size_bytes: NotRequired[
        "aws_sdk_dynamodb_streams.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The size of the stream record, in bytes.</p>"""
    stream_view_type: NotRequired[
        "aws_sdk_dynamodb_streams.types.stream_view_type.StreamViewType"
    ]
    """<p>The type of data from the modified DynamoDB item that was captured in this stream record:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - only the key attributes of the modified item.</p> </li> <li> <p> <code>NEW_IMAGE</code> - the entire item, as it appeared after it was modified.</p> </li> <li> <p> <code>OLD_IMAGE</code> - the entire item, as it appeared before it was modified.</p> </li> <li> <p> <code>NEW_AND_OLD_IMAGES</code> - both the new and the old item images of the item.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StreamRecord) -> dict:
    out: dict = {}
    if "approximate_creation_date_time" in value:
        import aws_sdk_dynamodb_streams.types.date

        out["ApproximateCreationDateTime"] = (
            aws_sdk_dynamodb_streams.types.date.serialize_aws_json_1_0(
                value["approximate_creation_date_time"]
            )
        )
    if "keys" in value:
        import aws_sdk_dynamodb_streams.types.attribute_map

        out["Keys"] = (
            aws_sdk_dynamodb_streams.types.attribute_map.serialize_aws_json_1_0(
                value["keys"]
            )
        )
    if "new_image" in value:
        import aws_sdk_dynamodb_streams.types.attribute_map

        out["NewImage"] = (
            aws_sdk_dynamodb_streams.types.attribute_map.serialize_aws_json_1_0(
                value["new_image"]
            )
        )
    if "old_image" in value:
        import aws_sdk_dynamodb_streams.types.attribute_map

        out["OldImage"] = (
            aws_sdk_dynamodb_streams.types.attribute_map.serialize_aws_json_1_0(
                value["old_image"]
            )
        )
    if "sequence_number" in value:
        out["SequenceNumber"] = value["sequence_number"]
    if "size_bytes" in value:
        out["SizeBytes"] = value["size_bytes"]
    if "stream_view_type" in value:
        import aws_sdk_dynamodb_streams.types.stream_view_type

        out["StreamViewType"] = (
            aws_sdk_dynamodb_streams.types.stream_view_type.serialize_aws_json_1_0(
                value["stream_view_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StreamRecord:
    out: StreamRecord = {}  # type: ignore[typeddict-item]
    if "ApproximateCreationDateTime" in data:
        import aws_sdk_dynamodb_streams.types.date

        out["approximate_creation_date_time"] = (
            aws_sdk_dynamodb_streams.types.date.deserialize_aws_json_1_0(
                data["ApproximateCreationDateTime"]
            )
        )
    if "Keys" in data:
        import aws_sdk_dynamodb_streams.types.attribute_map

        out["keys"] = (
            aws_sdk_dynamodb_streams.types.attribute_map.deserialize_aws_json_1_0(
                data["Keys"]
            )
        )
    if "NewImage" in data:
        import aws_sdk_dynamodb_streams.types.attribute_map

        out["new_image"] = (
            aws_sdk_dynamodb_streams.types.attribute_map.deserialize_aws_json_1_0(
                data["NewImage"]
            )
        )
    if "OldImage" in data:
        import aws_sdk_dynamodb_streams.types.attribute_map

        out["old_image"] = (
            aws_sdk_dynamodb_streams.types.attribute_map.deserialize_aws_json_1_0(
                data["OldImage"]
            )
        )
    if "SequenceNumber" in data:
        out["sequence_number"] = data["SequenceNumber"]
    if "SizeBytes" in data:
        out["size_bytes"] = data["SizeBytes"]
    if "StreamViewType" in data:
        import aws_sdk_dynamodb_streams.types.stream_view_type

        out["stream_view_type"] = (
            aws_sdk_dynamodb_streams.types.stream_view_type.deserialize_aws_json_1_0(
                data["StreamViewType"]
            )
        )
    return out
