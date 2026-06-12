"""Generated from Smithy shape ``com.amazonaws.glue#UpdateBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

UpdateBehavior: TypeAlias = Literal[
    "LOG",
    "UPDATE_IN_DATABASE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOG",
        "UPDATE_IN_DATABASE",
    )
)


def serialize_aws_json_1_1(value: UpdateBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateBehavior value: {data!r}")
    return cast(UpdateBehavior, data)
