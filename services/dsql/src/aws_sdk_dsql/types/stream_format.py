"""Generated from Smithy shape ``com.amazonaws.dsql#StreamFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dsql.errors import DeserializationError

"""<p>Stream record format.</p> <dl> <dt>JSON</dt> <dd> <p>Stream records are formatted as JSON.</p> </dd> </dl>"""
StreamFormat: TypeAlias = Literal["JSON",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("JSON",))


def serialize_json(value: StreamFormat) -> str:
    return value


def deserialize_json(data: str) -> StreamFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamFormat value: {data!r}")
    return cast(StreamFormat, data)
