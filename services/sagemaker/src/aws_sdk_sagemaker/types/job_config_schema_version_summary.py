"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobConfigSchemaVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_schema_version


class JobConfigSchemaVersionSummary(TypedDict):
    job_config_schema_version: NotRequired[
        "aws_sdk_sagemaker.types.job_schema_version.JobSchemaVersion"
    ]
    """<p>The version of the job configuration schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobConfigSchemaVersionSummary) -> dict:
    out: dict = {}
    if "job_config_schema_version" in value:
        out["JobConfigSchemaVersion"] = value["job_config_schema_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobConfigSchemaVersionSummary:
    out: JobConfigSchemaVersionSummary = {}  # type: ignore[typeddict-item]
    if "JobConfigSchemaVersion" in data:
        out["job_config_schema_version"] = data["JobConfigSchemaVersion"]
    return out
