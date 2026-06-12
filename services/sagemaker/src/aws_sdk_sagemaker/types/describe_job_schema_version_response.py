"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeJobSchemaVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_category
    import aws_sdk_sagemaker.types.job_config_document
    import aws_sdk_sagemaker.types.job_schema_version


class DescribeJobSchemaVersionResponse(TypedDict):
    job_category: NotRequired["aws_sdk_sagemaker.types.job_category.JobCategory"]
    """<p>The category of the job schema.</p>"""
    job_config_schema_version: NotRequired[
        "aws_sdk_sagemaker.types.job_schema_version.JobSchemaVersion"
    ]
    """<p>The version of the schema.</p>"""
    job_config_schema: NotRequired[
        "aws_sdk_sagemaker.types.job_config_document.JobConfigDocument"
    ]
    """<p>The JSON schema document that defines the structure of the job configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeJobSchemaVersionResponse) -> dict:
    out: dict = {}
    if "job_category" in value:
        import aws_sdk_sagemaker.types.job_category

        out["JobCategory"] = (
            aws_sdk_sagemaker.types.job_category.serialize_aws_json_1_1(
                value["job_category"]
            )
        )
    if "job_config_schema_version" in value:
        out["JobConfigSchemaVersion"] = value["job_config_schema_version"]
    if "job_config_schema" in value:
        out["JobConfigSchema"] = value["job_config_schema"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeJobSchemaVersionResponse:
    out: DescribeJobSchemaVersionResponse = {}  # type: ignore[typeddict-item]
    if "JobCategory" in data:
        import aws_sdk_sagemaker.types.job_category

        out["job_category"] = (
            aws_sdk_sagemaker.types.job_category.deserialize_aws_json_1_1(
                data["JobCategory"]
            )
        )
    if "JobConfigSchemaVersion" in data:
        out["job_config_schema_version"] = data["JobConfigSchemaVersion"]
    if "JobConfigSchema" in data:
        out["job_config_schema"] = data["JobConfigSchema"]
    return out
