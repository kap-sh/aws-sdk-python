"""Generated from Smithy shape ``com.amazonaws.ssm#PatchOrchestratorFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.patch_orchestrator_filter

PatchOrchestratorFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.patch_orchestrator_filter.PatchOrchestratorFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchOrchestratorFilterList) -> list:
    import aws_sdk_ssm.types.patch_orchestrator_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.patch_orchestrator_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PatchOrchestratorFilterList:
    import aws_sdk_ssm.types.patch_orchestrator_filter

    out: PatchOrchestratorFilterList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.patch_orchestrator_filter.deserialize_aws_json_1_1(item)
        )
    return out
