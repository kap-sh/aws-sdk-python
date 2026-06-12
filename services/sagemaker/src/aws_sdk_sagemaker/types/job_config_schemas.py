"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobConfigSchemas``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_config_schema_version_summary

JobConfigSchemas: TypeAlias = list[
    "aws_sdk_sagemaker.types.job_config_schema_version_summary.JobConfigSchemaVersionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobConfigSchemas) -> list:
    import aws_sdk_sagemaker.types.job_config_schema_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.job_config_schema_version_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> JobConfigSchemas:
    import aws_sdk_sagemaker.types.job_config_schema_version_summary

    out: JobConfigSchemas = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.job_config_schema_version_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
