"""Generated from Smithy shape ``com.amazonaws.evs#VmIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.vm_id

VmIdList: TypeAlias = list["aws_sdk_evs.types.vm_id.VmId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VmIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> VmIdList:
    return list(data)
