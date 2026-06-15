"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyValidationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

PolicyValidationMode: TypeAlias = Literal[
    "FAIL_ON_ANY_FINDINGS",
    "IGNORE_ALL_FINDINGS",
]

DEFAULT_POLICY_VALIDATION_MODE: PolicyValidationMode = "FAIL_ON_ANY_FINDINGS"

# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAIL_ON_ANY_FINDINGS",
        "IGNORE_ALL_FINDINGS",
    )
)


def serialize_json(value: PolicyValidationMode) -> str:
    return value


def deserialize_json(data: str) -> PolicyValidationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyValidationMode value: {data!r}")
    return cast(PolicyValidationMode, data)
