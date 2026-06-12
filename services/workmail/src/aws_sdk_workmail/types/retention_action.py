"""Generated from Smithy shape ``com.amazonaws.workmail#RetentionAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

RetentionAction: TypeAlias = Literal[
    "NONE",
    "DELETE",
    "PERMANENTLY_DELETE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "DELETE",
        "PERMANENTLY_DELETE",
    )
)


def serialize_aws_json_1_1(value: RetentionAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetentionAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetentionAction value: {data!r}")
    return cast(RetentionAction, data)
