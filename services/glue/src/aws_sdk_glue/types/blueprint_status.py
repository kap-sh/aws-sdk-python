"""Generated from Smithy shape ``com.amazonaws.glue#BlueprintStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

BlueprintStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: BlueprintStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlueprintStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlueprintStatus value: {data!r}")
    return cast(BlueprintStatus, data)
