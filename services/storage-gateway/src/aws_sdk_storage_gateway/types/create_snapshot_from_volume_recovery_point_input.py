"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateSnapshotFromVolumeRecoveryPointInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.snapshot_description
    import aws_sdk_storage_gateway.types.tags
    import aws_sdk_storage_gateway.types.volume_arn


class CreateSnapshotFromVolumeRecoveryPointInput(TypedDict):
    volume_arn: "aws_sdk_storage_gateway.types.volume_arn.VolumeARN"
    """<p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return to retrieve the TargetARN for specified VolumeARN.</p>"""
    snapshot_description: (
        "aws_sdk_storage_gateway.types.snapshot_description.SnapshotDescription"
    )
    """<p>Textual description of the snapshot that appears in the Amazon EC2 console, Elastic Block Store snapshots panel in the <b>Description</b> field, and in the Storage Gateway snapshot <b>Details</b> pane, <b>Description</b> field.</p>"""
    tags: NotRequired["aws_sdk_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotFromVolumeRecoveryPointInput) -> dict:
    out: dict = {}
    out["VolumeARN"] = value["volume_arn"]
    out["SnapshotDescription"] = value["snapshot_description"]
    if "tags" in value:
        import aws_sdk_storage_gateway.types.tags

        out["Tags"] = aws_sdk_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotFromVolumeRecoveryPointInput:
    out: CreateSnapshotFromVolumeRecoveryPointInput = {}  # type: ignore[typeddict-item]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    else:
        raise DeserializationError(
            "CreateSnapshotFromVolumeRecoveryPointInput.volume_arn required"
        )
    if "SnapshotDescription" in data:
        out["snapshot_description"] = data["SnapshotDescription"]
    else:
        raise DeserializationError(
            "CreateSnapshotFromVolumeRecoveryPointInput.snapshot_description required"
        )
    if "Tags" in data:
        import aws_sdk_storage_gateway.types.tags

        out["tags"] = aws_sdk_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
