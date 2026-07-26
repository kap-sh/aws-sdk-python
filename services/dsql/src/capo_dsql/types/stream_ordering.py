"""Generated from Smithy shape ``com.amazonaws.dsql#StreamOrdering``."""

from typing import Literal, TypeAlias, cast

"""<p>Stream ordering mode.</p> <dl> <dt>UNORDERED</dt> <dd> <p>Changes are streamed without ordering guarantees.</p> </dd> </dl>"""
StreamOrdering: TypeAlias = Literal["UNORDERED",]


# --- restJson1 ser/de ---
def serialize_json(value: StreamOrdering) -> str:
    return value


def deserialize_json(data: str) -> StreamOrdering:
    return cast(StreamOrdering, data)
