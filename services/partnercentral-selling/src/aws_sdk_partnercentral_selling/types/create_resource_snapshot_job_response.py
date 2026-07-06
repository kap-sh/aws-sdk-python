"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateResourceSnapshotJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_arn
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier


class CreateResourceSnapshotJobResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier"
    ]
    """<p>The unique identifier for the created snapshot job.</p>"""
    arn: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_job_arn.ResourceSnapshotJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the created snapshot job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateResourceSnapshotJobResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateResourceSnapshotJobResponse:
    out: CreateResourceSnapshotJobResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
