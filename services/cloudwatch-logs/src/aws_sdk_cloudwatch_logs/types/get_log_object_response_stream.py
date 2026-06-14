"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogObjectResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.errors.internal_streaming_exception
    import aws_sdk_cloudwatch_logs.types.fields_data


class _GetLogObjectResponseStream_fields(TypedDict):
    fields: "aws_sdk_cloudwatch_logs.types.fields_data.FieldsData"


class _GetLogObjectResponseStream_InternalStreamingException(TypedDict):
    InternalStreamingException: "aws_sdk_cloudwatch_logs.errors.internal_streaming_exception.InternalStreamingException_"


GetLogObjectResponseStream: TypeAlias = (
    _GetLogObjectResponseStream_fields
    | _GetLogObjectResponseStream_InternalStreamingException
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogObjectResponseStream) -> dict:
    if "fields" in value:
        import aws_sdk_cloudwatch_logs.types.fields_data

        return {
            "fields": aws_sdk_cloudwatch_logs.types.fields_data.serialize_aws_json_1_1(
                value["fields"]
            )
        }
    elif "InternalStreamingException" in value:
        import aws_sdk_cloudwatch_logs.errors.internal_streaming_exception

        return {
            "InternalStreamingException": aws_sdk_cloudwatch_logs.errors.internal_streaming_exception.serialize_aws_json_1_1(
                value["InternalStreamingException"]
            )
        }
    else:
        raise SerializationError("GetLogObjectResponseStream: no variant present")


def deserialize_aws_json_1_1(data: dict) -> GetLogObjectResponseStream:
    if "fields" in data:
        import aws_sdk_cloudwatch_logs.types.fields_data

        return {
            "fields": aws_sdk_cloudwatch_logs.types.fields_data.deserialize_aws_json_1_1(
                data["fields"]
            )
        }
    elif "InternalStreamingException" in data:
        import aws_sdk_cloudwatch_logs.errors.internal_streaming_exception

        return {
            "InternalStreamingException": aws_sdk_cloudwatch_logs.errors.internal_streaming_exception.deserialize_aws_json_1_1(
                data["InternalStreamingException"]
            )
        }
    else:
        raise DeserializationError(
            "GetLogObjectResponseStream: no recognized variant key"
        )
