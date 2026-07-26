"""Generated from Smithy shape ``com.amazonaws.sfn#ValidateStateMachineDefinitionResultCode``."""

from typing import Literal, TypeAlias, cast

ValidateStateMachineDefinitionResultCode: TypeAlias = Literal[
    "OK",
    "FAIL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidateStateMachineDefinitionResultCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidateStateMachineDefinitionResultCode:
    return cast(ValidateStateMachineDefinitionResultCode, data)
