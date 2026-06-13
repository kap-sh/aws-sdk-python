"""Generated from Smithy shape ``com.amazonaws.dsql#StreamStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dsql.errors import DeserializationError

"""<p>The current status of a stream.</p> <dl> <dt>CREATING</dt> <dd> <p>The stream is being created.</p> </dd> <dt>ACTIVE</dt> <dd> <p>The stream is active and processing changes.</p> </dd> <dt>DELETING</dt> <dd> <p>The stream is being deleted.</p> </dd> <dt>DELETED</dt> <dd> <p>The stream has been deleted.</p> </dd> <dt>FAILED</dt> <dd> <p>The stream has failed.</p> </dd> <dt>IMPAIRED</dt> <dd> <p>The stream is impaired and may not be processing changes correctly.</p> </dd> </dl>"""
StreamStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "DELETED",
    "FAILED",
    "IMPAIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "DELETED",
        "FAILED",
        "IMPAIRED",
    )
)


def serialize_json(value: StreamStatus) -> str:
    return value


def deserialize_json(data: str) -> StreamStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamStatus value: {data!r}")
    return cast(StreamStatus, data)
