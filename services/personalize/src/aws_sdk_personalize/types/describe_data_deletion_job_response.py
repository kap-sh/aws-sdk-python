"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDataDeletionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.data_deletion_job


class DescribeDataDeletionJobResponse(TypedDict, closed=True):
    data_deletion_job: NotRequired[
        "aws_sdk_personalize.types.data_deletion_job.DataDeletionJob"
    ]
    """<p>Information about the data deletion job, including the status.</p> <p>The status is one of the following values:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>IN_PROGRESS</p> </li> <li> <p>COMPLETED</p> </li> <li> <p>FAILED</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataDeletionJobResponse) -> dict:
    out: dict = {}
    if "data_deletion_job" in value:
        import aws_sdk_personalize.types.data_deletion_job

        out["dataDeletionJob"] = (
            aws_sdk_personalize.types.data_deletion_job.serialize_aws_json_1_1(
                value["data_deletion_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataDeletionJobResponse:
    out: DescribeDataDeletionJobResponse = {}  # type: ignore[typeddict-item]
    if "dataDeletionJob" in data:
        import aws_sdk_personalize.types.data_deletion_job

        out["data_deletion_job"] = (
            aws_sdk_personalize.types.data_deletion_job.deserialize_aws_json_1_1(
                data["dataDeletionJob"]
            )
        )
    return out
