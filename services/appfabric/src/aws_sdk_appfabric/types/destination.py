"""Generated from Smithy shape ``com.amazonaws.appfabric#Destination``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_appfabric.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.firehose_stream
    import aws_sdk_appfabric.types.s3_bucket


class _Destination_s3Bucket(TypedDict, closed=True):
    s3Bucket: "aws_sdk_appfabric.types.s3_bucket.S3Bucket"


class _Destination_firehoseStream(TypedDict, closed=True):
    firehoseStream: "aws_sdk_appfabric.types.firehose_stream.FirehoseStream"


Destination: TypeAlias = _Destination_s3Bucket | _Destination_firehoseStream


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    if "s3Bucket" in value:
        import aws_sdk_appfabric.types.s3_bucket

        return {
            "s3Bucket": aws_sdk_appfabric.types.s3_bucket.serialize_json(
                value["s3Bucket"]
            )
        }
    elif "firehoseStream" in value:
        import aws_sdk_appfabric.types.firehose_stream

        return {
            "firehoseStream": aws_sdk_appfabric.types.firehose_stream.serialize_json(
                value["firehoseStream"]
            )
        }
    else:
        raise SerializationError("Destination: no variant present")


def deserialize_json(data: dict) -> Destination:
    if "s3Bucket" in data:
        import aws_sdk_appfabric.types.s3_bucket

        return {
            "s3Bucket": aws_sdk_appfabric.types.s3_bucket.deserialize_json(
                data["s3Bucket"]
            )
        }
    elif "firehoseStream" in data:
        import aws_sdk_appfabric.types.firehose_stream

        return {
            "firehoseStream": aws_sdk_appfabric.types.firehose_stream.deserialize_json(
                data["firehoseStream"]
            )
        }
    else:
        raise DeserializationError("Destination: no recognized variant key")
