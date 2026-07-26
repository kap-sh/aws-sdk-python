"""Generated from Smithy shape ``com.amazonaws.tnb#DescriptorContentType``."""

from typing import Literal, TypeAlias, cast

DescriptorContentType: TypeAlias = Literal["text/plain",]


# --- restJson1 ser/de ---
def serialize_json(value: DescriptorContentType) -> str:
    return value


def deserialize_json(data: str) -> DescriptorContentType:
    return cast(DescriptorContentType, data)
