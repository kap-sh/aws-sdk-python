"""Generated from Smithy shape ``com.amazonaws.ssm#PatchGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch_group

PatchGroupList: TypeAlias = list["capo_ssm.types.patch_group.PatchGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchGroupList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PatchGroupList:
    return list(data)
