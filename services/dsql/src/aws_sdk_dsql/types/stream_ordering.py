"""Generated from Smithy shape ``com.amazonaws.dsql#StreamOrdering``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dsql.errors import DeserializationError

"""<p>Stream ordering mode.</p> <dl> <dt>UNORDERED</dt> <dd> <p>Changes are streamed without ordering guarantees.</p> </dd> </dl>"""
StreamOrdering: TypeAlias = Literal["UNORDERED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("UNORDERED",))


def serialize_json(value: StreamOrdering) -> str:
    return value


def deserialize_json(data: str) -> StreamOrdering:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamOrdering value: {data!r}")
    return cast(StreamOrdering, data)
