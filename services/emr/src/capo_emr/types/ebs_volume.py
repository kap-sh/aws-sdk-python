"""Generated from Smithy shape ``com.amazonaws.emr#EbsVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.string


class EbsVolume(TypedDict, closed=True):
    device: NotRequired["capo_emr.types.string.String"]
    """<p>The device name that is exposed to the instance, such as /dev/sdh.</p>"""
    volume_id: NotRequired["capo_emr.types.string.String"]
    """<p>The volume identifier of the EBS volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EbsVolume) -> dict:
    out: dict = {}
    if "device" in value:
        out["Device"] = value["device"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EbsVolume:
    out: EbsVolume = {}  # type: ignore[typeddict-item]
    if "Device" in data:
        out["device"] = data["Device"]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    return out
