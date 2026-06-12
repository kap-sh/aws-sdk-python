"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_category
    import aws_sdk_sagemaker.types.job_config_document
    import aws_sdk_sagemaker.types.job_name
    import aws_sdk_sagemaker.types.job_schema_version
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.tag_list


class CreateJobRequest(TypedDict):
    job_name: NotRequired["aws_sdk_sagemaker.types.job_name.JobName"]
    """<p>The name of the job. The name must be unique within your account and Amazon Web Services Region.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker assumes to perform the job. The role must have the necessary permissions to access the resources required by the job configuration.</p>"""
    job_category: NotRequired["aws_sdk_sagemaker.types.job_category.JobCategory"]
    """<p>The category of the job. The category determines the type of workload that the job runs.</p>"""
    job_config_schema_version: NotRequired[
        "aws_sdk_sagemaker.types.job_schema_version.JobSchemaVersion"
    ]
    """<p>The version of the configuration schema to use for the job configuration document. Use <code>ListJobSchemaVersions</code> to get available schema versions for a job category.</p>"""
    job_config_document: NotRequired[
        "aws_sdk_sagemaker.types.job_config_document.JobConfigDocument"
    ]
    """<p>The JSON configuration document for the job. The document must conform to the schema specified by <code>JobConfigSchemaVersion</code>. Use <code>DescribeJobSchemaVersion</code> to retrieve the schema for validation.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs to apply to the job as tags. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "job_category" in value:
        import aws_sdk_sagemaker.types.job_category

        out["JobCategory"] = (
            aws_sdk_sagemaker.types.job_category.serialize_aws_json_1_1(
                value["job_category"]
            )
        )
    if "job_config_schema_version" in value:
        out["JobConfigSchemaVersion"] = value["job_config_schema_version"]
    if "job_config_document" in value:
        out["JobConfigDocument"] = value["job_config_document"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "JobCategory" in data:
        import aws_sdk_sagemaker.types.job_category

        out["job_category"] = (
            aws_sdk_sagemaker.types.job_category.deserialize_aws_json_1_1(
                data["JobCategory"]
            )
        )
    if "JobConfigSchemaVersion" in data:
        out["job_config_schema_version"] = data["JobConfigSchemaVersion"]
    if "JobConfigDocument" in data:
        out["job_config_document"] = data["JobConfigDocument"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
