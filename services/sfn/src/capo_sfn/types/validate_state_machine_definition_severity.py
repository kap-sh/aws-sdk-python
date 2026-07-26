"""Generated from Smithy shape ``com.amazonaws.sfn#ValidateStateMachineDefinitionSeverity``."""

from typing import Literal, TypeAlias, cast

ValidateStateMachineDefinitionSeverity: TypeAlias = Literal[
    "ERROR",
    "WARNING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidateStateMachineDefinitionSeverity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidateStateMachineDefinitionSeverity:
    return cast(ValidateStateMachineDefinitionSeverity, data)
