"""Generated from Smithy shape ``com.amazonaws.codedeploy#EC2TagFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

EC2TagFilterType: TypeAlias = Literal[
    "KEY_ONLY",
    "VALUE_ONLY",
    "KEY_AND_VALUE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KEY_ONLY",
        "VALUE_ONLY",
        "KEY_AND_VALUE",
    )
)


def serialize_aws_json_1_1(value: EC2TagFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EC2TagFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EC2TagFilterType value: {data!r}")
    return cast(EC2TagFilterType, data)
