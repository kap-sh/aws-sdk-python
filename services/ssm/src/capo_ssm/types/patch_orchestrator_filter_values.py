"""Generated from Smithy shape ``com.amazonaws.ssm#PatchOrchestratorFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch_orchestrator_filter_value

PatchOrchestratorFilterValues: TypeAlias = list[
    "capo_ssm.types.patch_orchestrator_filter_value.PatchOrchestratorFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchOrchestratorFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PatchOrchestratorFilterValues:
    return list(data)
