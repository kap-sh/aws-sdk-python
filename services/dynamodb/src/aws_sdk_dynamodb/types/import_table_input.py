"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportTableInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.client_token
    import aws_sdk_dynamodb.types.input_compression_type
    import aws_sdk_dynamodb.types.input_format
    import aws_sdk_dynamodb.types.input_format_options
    import aws_sdk_dynamodb.types.s3_bucket_source
    import aws_sdk_dynamodb.types.table_creation_parameters


class ImportTableInput(TypedDict):
    client_token: NotRequired["aws_sdk_dynamodb.types.client_token.ClientToken"]
    """<p>Providing a <code>ClientToken</code> makes the call to <code>ImportTableInput</code> idempotent, meaning that multiple identical calls have the same effect as one single call.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After 8 hours, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 8 hours, or the result might not be idempotent.</p> <p>If you submit a request with the same client token but a change in other parameters within the 8-hour idempotency window, DynamoDB returns an <code>IdempotentParameterMismatch</code> exception.</p>"""
    s3_bucket_source: "aws_sdk_dynamodb.types.s3_bucket_source.S3BucketSource"
    """<p> The S3 bucket that provides the source for the import. </p>"""
    input_format: "aws_sdk_dynamodb.types.input_format.InputFormat"
    """<p> The format of the source data. Valid values for <code>ImportFormat</code> are <code>CSV</code>, <code>DYNAMODB_JSON</code> or <code>ION</code>. </p>"""
    input_format_options: NotRequired[
        "aws_sdk_dynamodb.types.input_format_options.InputFormatOptions"
    ]
    """<p> Additional properties that specify how the input is formatted, </p>"""
    input_compression_type: NotRequired[
        "aws_sdk_dynamodb.types.input_compression_type.InputCompressionType"
    ]
    """<p> Type of compression to be used on the input coming from the imported table. </p>"""
    table_creation_parameters: (
        "aws_sdk_dynamodb.types.table_creation_parameters.TableCreationParameters"
    )
    """<p>Parameters for the table to import the data into. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportTableInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import aws_sdk_dynamodb.types.s3_bucket_source

    out["S3BucketSource"] = (
        aws_sdk_dynamodb.types.s3_bucket_source.serialize_aws_json_1_0(
            value["s3_bucket_source"]
        )
    )
    import aws_sdk_dynamodb.types.input_format

    out["InputFormat"] = aws_sdk_dynamodb.types.input_format.serialize_aws_json_1_0(
        value["input_format"]
    )
    if "input_format_options" in value:
        import aws_sdk_dynamodb.types.input_format_options

        out["InputFormatOptions"] = (
            aws_sdk_dynamodb.types.input_format_options.serialize_aws_json_1_0(
                value["input_format_options"]
            )
        )
    if "input_compression_type" in value:
        import aws_sdk_dynamodb.types.input_compression_type

        out["InputCompressionType"] = (
            aws_sdk_dynamodb.types.input_compression_type.serialize_aws_json_1_0(
                value["input_compression_type"]
            )
        )
    import aws_sdk_dynamodb.types.table_creation_parameters

    out["TableCreationParameters"] = (
        aws_sdk_dynamodb.types.table_creation_parameters.serialize_aws_json_1_0(
            value["table_creation_parameters"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportTableInput:
    out: ImportTableInput = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "S3BucketSource" in data:
        import aws_sdk_dynamodb.types.s3_bucket_source

        out["s3_bucket_source"] = (
            aws_sdk_dynamodb.types.s3_bucket_source.deserialize_aws_json_1_0(
                data["S3BucketSource"]
            )
        )
    else:
        raise DeserializationError("ImportTableInput.s3_bucket_source required")
    if "InputFormat" in data:
        import aws_sdk_dynamodb.types.input_format

        out["input_format"] = (
            aws_sdk_dynamodb.types.input_format.deserialize_aws_json_1_0(
                data["InputFormat"]
            )
        )
    else:
        raise DeserializationError("ImportTableInput.input_format required")
    if "InputFormatOptions" in data:
        import aws_sdk_dynamodb.types.input_format_options

        out["input_format_options"] = (
            aws_sdk_dynamodb.types.input_format_options.deserialize_aws_json_1_0(
                data["InputFormatOptions"]
            )
        )
    if "InputCompressionType" in data:
        import aws_sdk_dynamodb.types.input_compression_type

        out["input_compression_type"] = (
            aws_sdk_dynamodb.types.input_compression_type.deserialize_aws_json_1_0(
                data["InputCompressionType"]
            )
        )
    if "TableCreationParameters" in data:
        import aws_sdk_dynamodb.types.table_creation_parameters

        out["table_creation_parameters"] = (
            aws_sdk_dynamodb.types.table_creation_parameters.deserialize_aws_json_1_0(
                data["TableCreationParameters"]
            )
        )
    else:
        raise DeserializationError(
            "ImportTableInput.table_creation_parameters required"
        )
    return out
