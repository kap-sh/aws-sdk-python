"""Generated from Smithy shape ``com.amazonaws.acmpca#FailureReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

FailureReason: TypeAlias = Literal[
    "REQUEST_TIMED_OUT",
    "UNSUPPORTED_ALGORITHM",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUEST_TIMED_OUT",
        "UNSUPPORTED_ALGORITHM",
        "OTHER",
    )
)


def serialize_aws_json_1_1(value: FailureReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailureReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailureReason value: {data!r}")
    return cast(FailureReason, data)
