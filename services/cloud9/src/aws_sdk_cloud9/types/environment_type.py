"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloud9.errors import DeserializationError

EnvironmentType: TypeAlias = Literal[
    "ssh",
    "ec2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ssh",
        "ec2",
    )
)


def serialize_aws_json_1_1(value: EnvironmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentType value: {data!r}")
    return cast(EnvironmentType, data)
