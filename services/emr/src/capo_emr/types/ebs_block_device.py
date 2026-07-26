"""Generated from Smithy shape ``com.amazonaws.emr#EbsBlockDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.string
    import capo_emr.types.volume_specification


class EbsBlockDevice(TypedDict, closed=True):
    volume_specification: NotRequired[
        "capo_emr.types.volume_specification.VolumeSpecification"
    ]
    """<p>EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.</p>"""
    device: NotRequired["capo_emr.types.string.String"]
    """<p>The device name that is exposed to the instance, such as /dev/sdh.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EbsBlockDevice) -> dict:
    out: dict = {}
    if "volume_specification" in value:
        import capo_emr.types.volume_specification

        out["VolumeSpecification"] = (
            capo_emr.types.volume_specification.serialize_aws_json_1_1(
                value["volume_specification"]
            )
        )
    if "device" in value:
        out["Device"] = value["device"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EbsBlockDevice:
    out: EbsBlockDevice = {}  # type: ignore[typeddict-item]
    if "VolumeSpecification" in data:
        import capo_emr.types.volume_specification

        out["volume_specification"] = (
            capo_emr.types.volume_specification.deserialize_aws_json_1_1(
                data["VolumeSpecification"]
            )
        )
    if "Device" in data:
        out["device"] = data["Device"]
    return out
