"""Generated from Smithy shape ``com.amazonaws.memorydb#InputAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_memorydb.errors import DeserializationError

InputAuthenticationType: TypeAlias = Literal[
    "password",
    "iam",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "password",
        "iam",
    )
)


def serialize_aws_json_1_1(value: InputAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputAuthenticationType value: {data!r}")
    return cast(InputAuthenticationType, data)
