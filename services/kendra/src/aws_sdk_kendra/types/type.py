"""Generated from Smithy shape ``com.amazonaws.kendra#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

Type: TypeAlias = Literal[
    "SAAS",
    "ON_PREMISE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAAS",
        "ON_PREMISE",
    )
)


def serialize_aws_json_1_1(value: Type) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)
