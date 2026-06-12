"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#Monotonicity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

Monotonicity: TypeAlias = Literal[
    "DECREASING",
    "INCREASING",
    "STATIC",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DECREASING",
        "INCREASING",
        "STATIC",
    )
)


def serialize_aws_json_1_0(value: Monotonicity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Monotonicity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Monotonicity value: {data!r}")
    return cast(Monotonicity, data)
