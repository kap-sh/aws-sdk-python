"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateResourceSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.resource_arn
    import aws_sdk_partnercentral_selling.types.resource_snapshot_revision


class CreateResourceSnapshotResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_partnercentral_selling.types.resource_arn.ResourceArn"]
    """<p> Specifies the Amazon Resource Name (ARN) that uniquely identifies the snapshot created. </p>"""
    revision: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_revision.ResourceSnapshotRevision"
    ]
    """<p> Specifies the revision number of the created snapshot. This field provides important information about the snapshot's place in the sequence of snapshots for the given resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateResourceSnapshotResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "revision" in value:
        out["Revision"] = value["revision"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateResourceSnapshotResponse:
    out: CreateResourceSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Revision" in data:
        out["revision"] = data["Revision"]
    return out
