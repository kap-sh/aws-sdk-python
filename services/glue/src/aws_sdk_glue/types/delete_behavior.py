"""Generated from Smithy shape ``com.amazonaws.glue#DeleteBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DeleteBehavior: TypeAlias = Literal[
    "LOG",
    "DELETE_FROM_DATABASE",
    "DEPRECATE_IN_DATABASE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOG",
        "DELETE_FROM_DATABASE",
        "DEPRECATE_IN_DATABASE",
    )
)


def serialize_aws_json_1_1(value: DeleteBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeleteBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeleteBehavior value: {data!r}")
    return cast(DeleteBehavior, data)
