"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#FormatConfigKey``."""

from typing import Literal, TypeAlias, cast

FormatConfigKey: TypeAlias = Literal["JPEGQuality",]


# --- restJson1 ser/de ---
def serialize_json(value: FormatConfigKey) -> str:
    return value


def deserialize_json(data: str) -> FormatConfigKey:
    return cast(FormatConfigKey, data)
