"""Generated from Smithy shape ``com.amazonaws.kendra#UserContextPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

UserContextPolicy: TypeAlias = Literal[
    "ATTRIBUTE_FILTER",
    "USER_TOKEN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATTRIBUTE_FILTER",
        "USER_TOKEN",
    )
)


def serialize_aws_json_1_1(value: UserContextPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserContextPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserContextPolicy value: {data!r}")
    return cast(UserContextPolicy, data)
