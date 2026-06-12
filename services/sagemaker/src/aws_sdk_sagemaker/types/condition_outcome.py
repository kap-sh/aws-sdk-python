"""Generated from Smithy shape ``com.amazonaws.sagemaker#ConditionOutcome``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ConditionOutcome: TypeAlias = Literal[
    "True",
    "False",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "True",
        "False",
    )
)


def serialize_aws_json_1_1(value: ConditionOutcome) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConditionOutcome:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConditionOutcome value: {data!r}")
    return cast(ConditionOutcome, data)
