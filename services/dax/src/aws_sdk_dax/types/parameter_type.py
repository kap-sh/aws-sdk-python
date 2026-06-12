"""Generated from Smithy shape ``com.amazonaws.dax#ParameterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dax.errors import DeserializationError

ParameterType: TypeAlias = Literal[
    "DEFAULT",
    "NODE_TYPE_SPECIFIC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "NODE_TYPE_SPECIFIC",
    )
)


def serialize_aws_json_1_1(value: ParameterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParameterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParameterType value: {data!r}")
    return cast(ParameterType, data)
