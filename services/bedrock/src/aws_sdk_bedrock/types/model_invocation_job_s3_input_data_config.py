"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobS3InputDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.account_id
    import aws_sdk_bedrock.types.s3_input_format
    import aws_sdk_bedrock.types.s3_uri


class ModelInvocationJobS3InputDataConfig(TypedDict):
    s3_input_format: NotRequired["aws_sdk_bedrock.types.s3_input_format.S3InputFormat"]
    """<p>The format of the input data.</p>"""
    s3_uri: "aws_sdk_bedrock.types.s3_uri.S3Uri"
    """<p>The S3 location of the input data.</p>"""
    s3_bucket_owner: NotRequired["aws_sdk_bedrock.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that owns the S3 bucket containing the input data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobS3InputDataConfig) -> dict:
    out: dict = {}
    if "s3_input_format" in value:
        import aws_sdk_bedrock.types.s3_input_format

        out["s3InputFormat"] = aws_sdk_bedrock.types.s3_input_format.serialize_json(
            value["s3_input_format"]
        )
    out["s3Uri"] = value["s3_uri"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    return out


def deserialize_json(data: dict) -> ModelInvocationJobS3InputDataConfig:
    out: ModelInvocationJobS3InputDataConfig = {}  # type: ignore[typeddict-item]
    if "s3InputFormat" in data:
        import aws_sdk_bedrock.types.s3_input_format

        out["s3_input_format"] = aws_sdk_bedrock.types.s3_input_format.deserialize_json(
            data["s3InputFormat"]
        )
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError(
            "ModelInvocationJobS3InputDataConfig.s3_uri required"
        )
    if "s3BucketOwner" in data:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    return out
