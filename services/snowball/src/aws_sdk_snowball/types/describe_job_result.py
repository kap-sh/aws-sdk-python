"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeJobResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.job_metadata
    import aws_sdk_snowball.types.job_metadata_list


class DescribeJobResult(TypedDict, closed=True):
    job_metadata: NotRequired["aws_sdk_snowball.types.job_metadata.JobMetadata"]
    """<p>Information about a specific job, including shipping information, job status, and other important metadata.</p>"""
    sub_job_metadata: NotRequired[
        "aws_sdk_snowball.types.job_metadata_list.JobMetadataList"
    ]
    """<p>Information about a specific job part (in the case of an export job), including shipping information, job status, and other important metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeJobResult) -> dict:
    out: dict = {}
    if "job_metadata" in value:
        import aws_sdk_snowball.types.job_metadata

        out["JobMetadata"] = aws_sdk_snowball.types.job_metadata.serialize_aws_json_1_1(
            value["job_metadata"]
        )
    if "sub_job_metadata" in value:
        import aws_sdk_snowball.types.job_metadata_list

        out["SubJobMetadata"] = (
            aws_sdk_snowball.types.job_metadata_list.serialize_aws_json_1_1(
                value["sub_job_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeJobResult:
    out: DescribeJobResult = {}  # type: ignore[typeddict-item]
    if "JobMetadata" in data:
        import aws_sdk_snowball.types.job_metadata

        out["job_metadata"] = (
            aws_sdk_snowball.types.job_metadata.deserialize_aws_json_1_1(
                data["JobMetadata"]
            )
        )
    if "SubJobMetadata" in data:
        import aws_sdk_snowball.types.job_metadata_list

        out["sub_job_metadata"] = (
            aws_sdk_snowball.types.job_metadata_list.deserialize_aws_json_1_1(
                data["SubJobMetadata"]
            )
        )
    return out
