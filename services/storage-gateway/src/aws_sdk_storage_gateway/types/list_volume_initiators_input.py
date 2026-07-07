"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListVolumeInitiatorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.volume_arn


class ListVolumeInitiatorsInput(TypedDict, closed=True):
    volume_arn: "aws_sdk_storage_gateway.types.volume_arn.VolumeARN"
    """<p>The Amazon Resource Name (ARN) of the volume. Use the <a>ListVolumes</a> operation to return a list of gateway volumes for the gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVolumeInitiatorsInput) -> dict:
    out: dict = {}
    out["VolumeARN"] = value["volume_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVolumeInitiatorsInput:
    out: ListVolumeInitiatorsInput = {}  # type: ignore[typeddict-item]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    else:
        raise DeserializationError("ListVolumeInitiatorsInput.volume_arn required")
    return out
