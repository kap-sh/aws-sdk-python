"""Generated from Smithy shape ``com.amazonaws.b2bi#X12TechnicalAcknowledgment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

X12TechnicalAcknowledgment: TypeAlias = Literal[
    "DO_NOT_GENERATE",
    "GENERATE_ALL_SEGMENTS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DO_NOT_GENERATE",
        "GENERATE_ALL_SEGMENTS",
    )
)


def serialize_aws_json_1_0(value: X12TechnicalAcknowledgment) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> X12TechnicalAcknowledgment:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown X12TechnicalAcknowledgment value: {data!r}"
        )
    return cast(X12TechnicalAcknowledgment, data)
