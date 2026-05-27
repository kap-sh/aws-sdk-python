"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateFunctionCodeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.architectures_list
    import aws_sdk_lambda.types.blob
    import aws_sdk_lambda.types.boolean
    import aws_sdk_lambda.types.function_name
    import aws_sdk_lambda.types.function_version_latest_published
    import aws_sdk_lambda.types.kms_key_arn
    import aws_sdk_lambda.types.s3_bucket
    import aws_sdk_lambda.types.s3_key
    import aws_sdk_lambda.types.s3_object_version
    import aws_sdk_lambda.types.string


class UpdateFunctionCodeRequest(TypedDict):
    function_name: "aws_sdk_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    zip_file: NotRequired["aws_sdk_lambda.types.blob.Blob"]
    """<p>The base64-encoded contents of the deployment package. Amazon Web Services SDK and CLI clients handle the encoding for you. Use only with a function defined with a .zip file archive deployment package.</p>"""
    s3_bucket: NotRequired["aws_sdk_lambda.types.s3_bucket.S3Bucket"]
    """<p>An Amazon S3 bucket in the same Amazon Web Services Region as your function. The bucket can be in a different Amazon Web Services account. Use only with a function defined with a .zip file archive deployment package.</p>"""
    s3_key: NotRequired["aws_sdk_lambda.types.s3_key.S3Key"]
    """<p>The Amazon S3 key of the deployment package. Use only with a function defined with a .zip file archive deployment package.</p>"""
    s3_object_version: NotRequired[
        "aws_sdk_lambda.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>For versioned objects, the version of the deployment package object to use.</p>"""
    image_uri: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>URI of a container image in the Amazon ECR registry. Do not use for a function defined with a .zip file archive.</p>"""
    publish: "aws_sdk_lambda.types.boolean.Boolean"
    """<p>Set to true to publish a new version of the function after updating the code. This has the same effect as calling <a>PublishVersion</a> separately.</p>"""
    dry_run: "aws_sdk_lambda.types.boolean.Boolean"
    """<p>Set to true to validate the request parameters and access permissions without modifying the function code.</p>"""
    revision_id: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.</p>"""
    architectures: NotRequired[
        "aws_sdk_lambda.types.architectures_list.ArchitecturesList"
    ]
    """<p>The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is <code>x86_64</code>.</p>"""
    source_kms_key_arn: NotRequired["aws_sdk_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt your function's .zip deployment package. If you don't provide a customer managed key, Lambda uses an Amazon Web Services managed key.</p>"""
    publish_to: NotRequired[
        "aws_sdk_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
    ]
    """<p>Specifies where to publish the function version or configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFunctionCodeRequest) -> dict:
    out: dict = {}
    if "zip_file" in value:
        import aws_sdk_lambda.types.blob

        out["ZipFile"] = aws_sdk_lambda.types.blob.serialize_json(value["zip_file"])
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    if "s3_object_version" in value:
        out["S3ObjectVersion"] = value["s3_object_version"]
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    out["Publish"] = value.get("publish", False)
    out["DryRun"] = value.get("dry_run", False)
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    if "architectures" in value:
        import aws_sdk_lambda.types.architectures_list

        out["Architectures"] = aws_sdk_lambda.types.architectures_list.serialize_json(
            value["architectures"]
        )
    if "source_kms_key_arn" in value:
        out["SourceKMSKeyArn"] = value["source_kms_key_arn"]
    if "publish_to" in value:
        import aws_sdk_lambda.types.function_version_latest_published

        out["PublishTo"] = (
            aws_sdk_lambda.types.function_version_latest_published.serialize_json(
                value["publish_to"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateFunctionCodeRequest:
    out: UpdateFunctionCodeRequest = {}  # type: ignore[typeddict-item]
    if "ZipFile" in data:
        import aws_sdk_lambda.types.blob

        out["zip_file"] = aws_sdk_lambda.types.blob.deserialize_json(data["ZipFile"])
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    if "S3Key" in data:
        out["s3_key"] = data["S3Key"]
    if "S3ObjectVersion" in data:
        out["s3_object_version"] = data["S3ObjectVersion"]
    if "ImageUri" in data:
        out["image_uri"] = data["ImageUri"]
    if "Publish" in data:
        out["publish"] = data["Publish"]
    else:
        out["publish"] = False
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    if "Architectures" in data:
        import aws_sdk_lambda.types.architectures_list

        out["architectures"] = aws_sdk_lambda.types.architectures_list.deserialize_json(
            data["Architectures"]
        )
    if "SourceKMSKeyArn" in data:
        out["source_kms_key_arn"] = data["SourceKMSKeyArn"]
    if "PublishTo" in data:
        import aws_sdk_lambda.types.function_version_latest_published

        out["publish_to"] = (
            aws_sdk_lambda.types.function_version_latest_published.deserialize_json(
                data["PublishTo"]
            )
        )
    return out
