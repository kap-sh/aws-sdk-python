"""Generated from Smithy shape ``com.amazonaws.ssm#PatchGroupPatchBaselineMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch_group_patch_baseline_mapping

PatchGroupPatchBaselineMappingList: TypeAlias = list[
    "capo_ssm.types.patch_group_patch_baseline_mapping.PatchGroupPatchBaselineMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchGroupPatchBaselineMappingList) -> list:
    import capo_ssm.types.patch_group_patch_baseline_mapping

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.patch_group_patch_baseline_mapping.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PatchGroupPatchBaselineMappingList:
    import capo_ssm.types.patch_group_patch_baseline_mapping

    out: PatchGroupPatchBaselineMappingList = []
    for item in data:
        out.append(
            capo_ssm.types.patch_group_patch_baseline_mapping.deserialize_aws_json_1_1(
                item
            )
        )
    return out
