"""Generated from Smithy shape ``com.amazonaws.ssm#PatchIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch_id

PatchIdList: TypeAlias = list["capo_ssm.types.patch_id.PatchId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PatchIdList:
    return list(data)
