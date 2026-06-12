"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Currency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

Currency: TypeAlias = Literal[
    "USD",
    "CNY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USD",
        "CNY",
    )
)


def serialize_aws_json_1_0(value: Currency) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Currency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Currency value: {data!r}")
    return cast(Currency, data)
