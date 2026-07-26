"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_compute_optimizer_automation.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.ebs_volume


class _ResourceDetails_ebsVolume(TypedDict, closed=True):
    ebsVolume: "capo_compute_optimizer_automation.types.ebs_volume.EbsVolume"


ResourceDetails: TypeAlias = _ResourceDetails_ebsVolume


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceDetails) -> dict:
    if "ebsVolume" in value:
        import capo_compute_optimizer_automation.types.ebs_volume

        return {
            "ebsVolume": capo_compute_optimizer_automation.types.ebs_volume.serialize_aws_json_1_0(
                value["ebsVolume"]
            )
        }
    else:
        raise SerializationError("ResourceDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ResourceDetails:
    if "ebsVolume" in data:
        import capo_compute_optimizer_automation.types.ebs_volume

        return {
            "ebsVolume": capo_compute_optimizer_automation.types.ebs_volume.deserialize_aws_json_1_0(
                data["ebsVolume"]
            )
        }
    else:
        raise DeserializationError("ResourceDetails: no recognized variant key")
