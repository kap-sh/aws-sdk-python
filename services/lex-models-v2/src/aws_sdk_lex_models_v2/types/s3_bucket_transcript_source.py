"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#S3BucketTranscriptSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.kms_key_arn
    import aws_sdk_lex_models_v2.types.path_format
    import aws_sdk_lex_models_v2.types.s3_bucket_name
    import aws_sdk_lex_models_v2.types.transcript_filter
    import aws_sdk_lex_models_v2.types.transcript_format


class S3BucketTranscriptSource(TypedDict, closed=True):
    s3_bucket_name: "aws_sdk_lex_models_v2.types.s3_bucket_name.S3BucketName"
    """<p>The name of the bucket containing the transcript and the associated metadata.</p>"""
    path_format: NotRequired["aws_sdk_lex_models_v2.types.path_format.PathFormat"]
    """<p>The object that contains a path format that will be applied when Amazon Lex reads the transcript file in the bucket you provide. Specify this object if you only want Lex to read a subset of files in your Amazon S3 bucket.</p>"""
    transcript_format: "aws_sdk_lex_models_v2.types.transcript_format.TranscriptFormat"
    """<p>The format of the transcript content. Currently, Genie only supports the Amazon Lex transcript format.</p>"""
    transcript_filter: NotRequired[
        "aws_sdk_lex_models_v2.types.transcript_filter.TranscriptFilter"
    ]
    """<p>The object that contains the filter which will be applied when Amazon Lex reads through the Amazon S3 bucket. Specify this object if you want Amazon Lex to read only a subset of the Amazon S3 bucket based on the filter you provide.</p>"""
    kms_key_arn: NotRequired["aws_sdk_lex_models_v2.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key that customer use to encrypt their Amazon S3 bucket. Only use this field if your bucket is encrypted using a customer managed KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketTranscriptSource) -> dict:
    out: dict = {}
    out["s3BucketName"] = value["s3_bucket_name"]
    if "path_format" in value:
        import aws_sdk_lex_models_v2.types.path_format

        out["pathFormat"] = aws_sdk_lex_models_v2.types.path_format.serialize_json(
            value["path_format"]
        )
    import aws_sdk_lex_models_v2.types.transcript_format

    out["transcriptFormat"] = (
        aws_sdk_lex_models_v2.types.transcript_format.serialize_json(
            value["transcript_format"]
        )
    )
    if "transcript_filter" in value:
        import aws_sdk_lex_models_v2.types.transcript_filter

        out["transcriptFilter"] = (
            aws_sdk_lex_models_v2.types.transcript_filter.serialize_json(
                value["transcript_filter"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> S3BucketTranscriptSource:
    out: S3BucketTranscriptSource = {}  # type: ignore[typeddict-item]
    if "s3BucketName" in data:
        out["s3_bucket_name"] = data["s3BucketName"]
    else:
        raise DeserializationError("S3BucketTranscriptSource.s3_bucket_name required")
    if "pathFormat" in data:
        import aws_sdk_lex_models_v2.types.path_format

        out["path_format"] = aws_sdk_lex_models_v2.types.path_format.deserialize_json(
            data["pathFormat"]
        )
    if "transcriptFormat" in data:
        import aws_sdk_lex_models_v2.types.transcript_format

        out["transcript_format"] = (
            aws_sdk_lex_models_v2.types.transcript_format.deserialize_json(
                data["transcriptFormat"]
            )
        )
    else:
        raise DeserializationError(
            "S3BucketTranscriptSource.transcript_format required"
        )
    if "transcriptFilter" in data:
        import aws_sdk_lex_models_v2.types.transcript_filter

        out["transcript_filter"] = (
            aws_sdk_lex_models_v2.types.transcript_filter.deserialize_json(
                data["transcriptFilter"]
            )
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
