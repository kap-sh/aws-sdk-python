"""Generated from Smithy shape ``com.amazonaws.emr#StepCancellationOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

StepCancellationOption: TypeAlias = Literal[
    "SEND_INTERRUPT",
    "TERMINATE_PROCESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEND_INTERRUPT",
        "TERMINATE_PROCESS",
    )
)


def serialize_aws_json_1_1(value: StepCancellationOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepCancellationOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepCancellationOption value: {data!r}")
    return cast(StepCancellationOption, data)
