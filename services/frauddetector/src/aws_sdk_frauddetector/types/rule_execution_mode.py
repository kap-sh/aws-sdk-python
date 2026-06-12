"""Generated from Smithy shape ``com.amazonaws.frauddetector#RuleExecutionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

RuleExecutionMode: TypeAlias = Literal[
    "ALL_MATCHED",
    "FIRST_MATCHED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_MATCHED",
        "FIRST_MATCHED",
    )
)


def serialize_aws_json_1_1(value: RuleExecutionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleExecutionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleExecutionMode value: {data!r}")
    return cast(RuleExecutionMode, data)
