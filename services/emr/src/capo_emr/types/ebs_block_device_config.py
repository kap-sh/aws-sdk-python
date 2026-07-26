"""Generated from Smithy shape ``com.amazonaws.emr#EbsBlockDeviceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.integer
    import capo_emr.types.volume_specification


class EbsBlockDeviceConfig(TypedDict, closed=True):
    volume_specification: NotRequired[
        "capo_emr.types.volume_specification.VolumeSpecification"
    ]
    """<p>EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.</p>"""
    volumes_per_instance: NotRequired["capo_emr.types.integer.Integer"]
    """<p>Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EbsBlockDeviceConfig) -> dict:
    out: dict = {}
    if "volume_specification" in value:
        import capo_emr.types.volume_specification

        out["VolumeSpecification"] = (
            capo_emr.types.volume_specification.serialize_aws_json_1_1(
                value["volume_specification"]
            )
        )
    if "volumes_per_instance" in value:
        out["VolumesPerInstance"] = value["volumes_per_instance"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EbsBlockDeviceConfig:
    out: EbsBlockDeviceConfig = {}  # type: ignore[typeddict-item]
    if "VolumeSpecification" in data:
        import capo_emr.types.volume_specification

        out["volume_specification"] = (
            capo_emr.types.volume_specification.deserialize_aws_json_1_1(
                data["VolumeSpecification"]
            )
        )
    if "VolumesPerInstance" in data:
        out["volumes_per_instance"] = data["VolumesPerInstance"]
    return out
