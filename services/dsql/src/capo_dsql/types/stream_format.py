"""Generated from Smithy shape ``com.amazonaws.dsql#StreamFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>Stream record format.</p> <dl> <dt>JSON</dt> <dd> <p>Stream records are formatted as JSON.</p> </dd> </dl>"""
StreamFormat: TypeAlias = Literal["JSON",]


# --- restJson1 ser/de ---
def serialize_json(value: StreamFormat) -> str:
    return value


def deserialize_json(data: str) -> StreamFormat:
    return cast(StreamFormat, data)
