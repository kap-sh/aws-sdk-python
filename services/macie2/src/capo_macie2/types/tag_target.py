"""Generated from Smithy shape ``com.amazonaws.macie2#TagTarget``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of object to apply a tag-based condition to. Valid values are:</p>"""
TagTarget: TypeAlias = Literal["S3_OBJECT",]


# --- restJson1 ser/de ---
def serialize_json(value: TagTarget) -> str:
    return value


def deserialize_json(data: str) -> TagTarget:
    return cast(TagTarget, data)
