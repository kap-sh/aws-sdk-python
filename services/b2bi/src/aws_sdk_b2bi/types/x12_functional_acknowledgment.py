"""Generated from Smithy shape ``com.amazonaws.b2bi#X12FunctionalAcknowledgment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

X12FunctionalAcknowledgment: TypeAlias = Literal[
    "DO_NOT_GENERATE",
    "GENERATE_ALL_SEGMENTS",
    "GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DO_NOT_GENERATE",
        "GENERATE_ALL_SEGMENTS",
        "GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP",
    )
)


def serialize_aws_json_1_0(value: X12FunctionalAcknowledgment) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> X12FunctionalAcknowledgment:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown X12FunctionalAcknowledgment value: {data!r}"
        )
    return cast(X12FunctionalAcknowledgment, data)
