"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectStorageServerProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

ObjectStorageServerProtocol: TypeAlias = Literal[
    "HTTPS",
    "HTTP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTPS",
        "HTTP",
    )
)


def serialize_aws_json_1_1(value: ObjectStorageServerProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectStorageServerProtocol:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ObjectStorageServerProtocol value: {data!r}"
        )
    return cast(ObjectStorageServerProtocol, data)
