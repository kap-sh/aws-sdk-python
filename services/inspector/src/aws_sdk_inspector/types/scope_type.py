"""Generated from Smithy shape ``com.amazonaws.inspector#ScopeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

ScopeType: TypeAlias = Literal[
    "INSTANCE_ID",
    "RULES_PACKAGE_ARN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTANCE_ID",
        "RULES_PACKAGE_ARN",
    )
)


def serialize_aws_json_1_1(value: ScopeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScopeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScopeType value: {data!r}")
    return cast(ScopeType, data)
