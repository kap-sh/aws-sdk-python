"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

InstanceType: TypeAlias = Literal[
    "Blue",
    "Green",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Blue",
        "Green",
    )
)


def serialize_aws_json_1_1(value: InstanceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceType value: {data!r}")
    return cast(InstanceType, data)
