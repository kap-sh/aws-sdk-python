"""Generated from Smithy shape ``com.amazonaws.ssm#PatchBugzillaIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch_bugzilla_id

PatchBugzillaIdList: TypeAlias = list[
    "capo_ssm.types.patch_bugzilla_id.PatchBugzillaId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchBugzillaIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PatchBugzillaIdList:
    return list(data)
