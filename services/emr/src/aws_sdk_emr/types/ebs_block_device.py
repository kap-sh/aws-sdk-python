"""Generated from Smithy shape ``com.amazonaws.emr#EbsBlockDevice``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.volume_specification


class EbsBlockDevice(TypedDict):
    volume_specification: NotRequired[
        "aws_sdk_emr.types.volume_specification.VolumeSpecification"
    ]
    """<p>EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.</p>"""
    device: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The device name that is exposed to the instance, such as /dev/sdh.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EbsBlockDevice) -> dict:
    out: dict = {}
    if "volume_specification" in value:
        import aws_sdk_emr.types.volume_specification

        out["VolumeSpecification"] = (
            aws_sdk_emr.types.volume_specification.serialize_aws_json_1_1(
                value["volume_specification"]
            )
        )
    if "device" in value:
        out["Device"] = value["device"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EbsBlockDevice:
    out: EbsBlockDevice = {}  # type: ignore[typeddict-item]
    if "VolumeSpecification" in data:
        import aws_sdk_emr.types.volume_specification

        out["volume_specification"] = (
            aws_sdk_emr.types.volume_specification.deserialize_aws_json_1_1(
                data["VolumeSpecification"]
            )
        )
    if "Device" in data:
        out["device"] = data["Device"]
    return out
