"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListJobSchemaVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_config_schemas
    import aws_sdk_sagemaker.types.next_token


class ListJobSchemaVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, this token retrieves the next set of results.</p>"""
    job_config_schemas: NotRequired[
        "aws_sdk_sagemaker.types.job_config_schemas.JobConfigSchemas"
    ]
    """<p>An array of <code>JobConfigSchemaVersionSummary</code> objects listing the available schema versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListJobSchemaVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "job_config_schemas" in value:
        import aws_sdk_sagemaker.types.job_config_schemas

        out["JobConfigSchemas"] = (
            aws_sdk_sagemaker.types.job_config_schemas.serialize_aws_json_1_1(
                value["job_config_schemas"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListJobSchemaVersionsResponse:
    out: ListJobSchemaVersionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "JobConfigSchemas" in data:
        import aws_sdk_sagemaker.types.job_config_schemas

        out["job_config_schemas"] = (
            aws_sdk_sagemaker.types.job_config_schemas.deserialize_aws_json_1_1(
                data["JobConfigSchemas"]
            )
        )
    return out
