"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDataDeletionJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class CreateDataDeletionJobResponse(TypedDict):
    data_deletion_job_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the data deletion job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataDeletionJobResponse) -> dict:
    out: dict = {}
    if "data_deletion_job_arn" in value:
        out["dataDeletionJobArn"] = value["data_deletion_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataDeletionJobResponse:
    out: CreateDataDeletionJobResponse = {}  # type: ignore[typeddict-item]
    if "dataDeletionJobArn" in data:
        out["data_deletion_job_arn"] = data["dataDeletionJobArn"]
    return out
