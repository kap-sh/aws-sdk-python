"""Generated from Smithy shape ``com.amazonaws.s3tables#OpenTableFormat``."""

from typing import Literal, TypeAlias, cast

OpenTableFormat: TypeAlias = Literal["ICEBERG",]


# --- restJson1 ser/de ---
def serialize_json(value: OpenTableFormat) -> str:
    return value


def deserialize_json(data: str) -> OpenTableFormat:
    return cast(OpenTableFormat, data)
