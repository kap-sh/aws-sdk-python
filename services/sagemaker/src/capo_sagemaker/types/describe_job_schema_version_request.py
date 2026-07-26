"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeJobSchemaVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.job_category
    import capo_sagemaker.types.job_schema_version


class DescribeJobSchemaVersionRequest(TypedDict, closed=True):
    job_category: NotRequired["capo_sagemaker.types.job_category.JobCategory"]
    """<p>The category of the job schema to describe.</p>"""
    job_config_schema_version: NotRequired[
        "capo_sagemaker.types.job_schema_version.JobSchemaVersion"
    ]
    """<p>The version of the schema to retrieve. If not specified, the latest version is returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeJobSchemaVersionRequest) -> dict:
    out: dict = {}
    if "job_category" in value:
        import capo_sagemaker.types.job_category

        out["JobCategory"] = capo_sagemaker.types.job_category.serialize_aws_json_1_1(
            value["job_category"]
        )
    if "job_config_schema_version" in value:
        out["JobConfigSchemaVersion"] = value["job_config_schema_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeJobSchemaVersionRequest:
    out: DescribeJobSchemaVersionRequest = {}  # type: ignore[typeddict-item]
    if "JobCategory" in data:
        import capo_sagemaker.types.job_category

        out["job_category"] = (
            capo_sagemaker.types.job_category.deserialize_aws_json_1_1(
                data["JobCategory"]
            )
        )
    if "JobConfigSchemaVersion" in data:
        out["job_config_schema_version"] = data["JobConfigSchemaVersion"]
    return out
