"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

ActionCategory: TypeAlias = Literal[
    "Source",
    "Build",
    "Deploy",
    "Test",
    "Invoke",
    "Approval",
    "Compute",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Source",
        "Build",
        "Deploy",
        "Test",
        "Invoke",
        "Approval",
        "Compute",
    )
)


def serialize_aws_json_1_1(value: ActionCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionCategory value: {data!r}")
    return cast(ActionCategory, data)
