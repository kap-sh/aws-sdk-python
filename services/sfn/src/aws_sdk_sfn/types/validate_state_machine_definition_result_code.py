"""Generated from Smithy shape ``com.amazonaws.sfn#ValidateStateMachineDefinitionResultCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

ValidateStateMachineDefinitionResultCode: TypeAlias = Literal[
    "OK",
    "FAIL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OK",
        "FAIL",
    )
)


def serialize_aws_json_1_0(value: ValidateStateMachineDefinitionResultCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidateStateMachineDefinitionResultCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ValidateStateMachineDefinitionResultCode value: {data!r}"
        )
    return cast(ValidateStateMachineDefinitionResultCode, data)
