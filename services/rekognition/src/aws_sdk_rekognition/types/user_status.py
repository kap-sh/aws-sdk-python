"""Generated from Smithy shape ``com.amazonaws.rekognition#UserStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

UserStatus: TypeAlias = Literal[
    "ACTIVE",
    "UPDATING",
    "CREATING",
    "CREATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "UPDATING",
        "CREATING",
        "CREATED",
    )
)


def serialize_aws_json_1_1(value: UserStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserStatus value: {data!r}")
    return cast(UserStatus, data)
