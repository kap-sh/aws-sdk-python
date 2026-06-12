"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetLabel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

TargetLabel: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: TargetLabel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetLabel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetLabel value: {data!r}")
    return cast(TargetLabel, data)
