"""Generated from Smithy shape ``com.amazonaws.sfn#ValidateStateMachineDefinitionSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

ValidateStateMachineDefinitionSeverity: TypeAlias = Literal[
    "ERROR",
    "WARNING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ERROR",
        "WARNING",
    )
)


def serialize_aws_json_1_0(value: ValidateStateMachineDefinitionSeverity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidateStateMachineDefinitionSeverity:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ValidateStateMachineDefinitionSeverity value: {data!r}"
        )
    return cast(ValidateStateMachineDefinitionSeverity, data)
