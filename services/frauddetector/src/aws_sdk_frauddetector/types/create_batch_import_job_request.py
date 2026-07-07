"""Generated from Smithy shape ``com.amazonaws.frauddetector#CreateBatchImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.iam_role_arn
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.s3_bucket_location
    import aws_sdk_frauddetector.types.tag_list


class CreateBatchImportJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The ID of the batch import job. The ID cannot be of a past job, unless the job exists in <code>CREATE_FAILED</code> state.</p>"""
    input_path: "aws_sdk_frauddetector.types.s3_bucket_location.s3BucketLocation"
    """<p>The URI that points to the Amazon S3 location of your data file.</p>"""
    output_path: "aws_sdk_frauddetector.types.s3_bucket_location.s3BucketLocation"
    """<p>The URI that points to the Amazon S3 location for storing your results. </p>"""
    event_type_name: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The name of the event type.</p>"""
    iam_role_arn: "aws_sdk_frauddetector.types.iam_role_arn.iamRoleArn"
    r"""<p>The ARN of the IAM role created for Amazon S3 bucket that holds your data file.</p> <p>The IAM role must have read permissions to your input S3 bucket and write permissions to your output S3 bucket. For more information about bucket permissions, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html\">User policy examples</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key-value pairs associated with this request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBatchImportJobRequest) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["inputPath"] = value["input_path"]
    out["outputPath"] = value["output_path"]
    out["eventTypeName"] = value["event_type_name"]
    out["iamRoleArn"] = value["iam_role_arn"]
    if "tags" in value:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBatchImportJobRequest:
    out: CreateBatchImportJobRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("CreateBatchImportJobRequest.job_id required")
    if "inputPath" in data:
        out["input_path"] = data["inputPath"]
    else:
        raise DeserializationError("CreateBatchImportJobRequest.input_path required")
    if "outputPath" in data:
        out["output_path"] = data["outputPath"]
    else:
        raise DeserializationError("CreateBatchImportJobRequest.output_path required")
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    else:
        raise DeserializationError(
            "CreateBatchImportJobRequest.event_type_name required"
        )
    if "iamRoleArn" in data:
        out["iam_role_arn"] = data["iamRoleArn"]
    else:
        raise DeserializationError("CreateBatchImportJobRequest.iam_role_arn required")
    if "tags" in data:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
