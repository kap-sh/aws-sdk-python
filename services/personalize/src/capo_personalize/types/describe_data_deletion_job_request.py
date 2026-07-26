"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDataDeletionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeDataDeletionJobRequest(TypedDict, closed=True):
    data_deletion_job_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data deletion job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataDeletionJobRequest) -> dict:
    out: dict = {}
    out["dataDeletionJobArn"] = value["data_deletion_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataDeletionJobRequest:
    out: DescribeDataDeletionJobRequest = {}  # type: ignore[typeddict-item]
    if "dataDeletionJobArn" in data:
        out["data_deletion_job_arn"] = data["dataDeletionJobArn"]
    else:
        raise DeserializationError(
            "DescribeDataDeletionJobRequest.data_deletion_job_arn required"
        )
    return out
