"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildResultAssetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "BUILD_LOG",
        "QUALITY_REPORT",
        "POLICY_DEFINITION",
        "GENERATED_TEST_CASES",
        "POLICY_SCENARIOS",
        "FIDELITY_REPORT",
        "ASSET_MANIFEST",
        "SOURCE_DOCUMENT",
    )
)


def serialize_json(value: AutomatedReasoningPolicyBuildResultAssetType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildResultAssetType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyBuildResultAssetType value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyBuildResultAssetType, data)
