"""Generated from Smithy shape ``com.amazonaws.appflow#WriteOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

"""<p> The possible write operations in the destination connector. When this value is not provided, this defaults to the <code>INSERT</code> operation. </p>"""
WriteOperationType: TypeAlias = Literal[
    "INSERT",
    "UPSERT",
    "UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSERT",
        "UPSERT",
        "UPDATE",
        "DELETE",
    )
)


def serialize_json(value: WriteOperationType) -> str:
    return value


def deserialize_json(data: str) -> WriteOperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WriteOperationType value: {data!r}")
    return cast(WriteOperationType, data)
