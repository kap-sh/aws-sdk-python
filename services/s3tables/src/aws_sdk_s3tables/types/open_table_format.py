"""Generated from Smithy shape ``com.amazonaws.s3tables#OpenTableFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

OpenTableFormat: TypeAlias = Literal["ICEBERG",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ICEBERG",))


def serialize_json(value: OpenTableFormat) -> str:
    return value


def deserialize_json(data: str) -> OpenTableFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpenTableFormat value: {data!r}")
    return cast(OpenTableFormat, data)
