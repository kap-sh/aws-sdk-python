"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteVolumeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.volume_arn


class DeleteVolumeOutput(TypedDict, closed=True):
    volume_arn: NotRequired["aws_sdk_storage_gateway.types.volume_arn.VolumeARN"]
    """<p>The Amazon Resource Name (ARN) of the storage volume that was deleted. It is the same ARN you provided in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVolumeOutput) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["VolumeARN"] = value["volume_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVolumeOutput:
    out: DeleteVolumeOutput = {}  # type: ignore[typeddict-item]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    return out
