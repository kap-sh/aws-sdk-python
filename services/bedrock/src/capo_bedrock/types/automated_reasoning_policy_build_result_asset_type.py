"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildResultAssetType``."""

from typing import Literal, TypeAlias, cast

AutomatedReasoningPolicyBuildResultAssetType: TypeAlias = Literal[
    "BUILD_LOG",
    "QUALITY_REPORT",
    "POLICY_DEFINITION",
    "GENERATED_TEST_CASES",
    "POLICY_SCENARIOS",
    "FIDELITY_REPORT",
    "ASSET_MANIFEST",
    "SOURCE_DOCUMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildResultAssetType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildResultAssetType:
    return cast(AutomatedReasoningPolicyBuildResultAssetType, data)
