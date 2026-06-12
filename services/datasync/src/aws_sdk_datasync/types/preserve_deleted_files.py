"""Generated from Smithy shape ``com.amazonaws.datasync#PreserveDeletedFiles``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

PreserveDeletedFiles: TypeAlias = Literal[
    "PRESERVE",
    "REMOVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRESERVE",
        "REMOVE",
    )
)


def serialize_aws_json_1_1(value: PreserveDeletedFiles) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreserveDeletedFiles:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreserveDeletedFiles value: {data!r}")
    return cast(PreserveDeletedFiles, data)
