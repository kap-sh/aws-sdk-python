"""Generated from Smithy shape ``com.amazonaws.ssm#PatchAdvisoryIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch_advisory_id

PatchAdvisoryIdList: TypeAlias = list[
    "capo_ssm.types.patch_advisory_id.PatchAdvisoryId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchAdvisoryIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PatchAdvisoryIdList:
    return list(data)
