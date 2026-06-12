"""Generated from Smithy shape ``com.amazonaws.macie2#TagTarget``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The type of object to apply a tag-based condition to. Valid values are:</p>"""
TagTarget: TypeAlias = Literal["S3_OBJECT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3_OBJECT",))


def serialize_json(value: TagTarget) -> str:
    return value


def deserialize_json(data: str) -> TagTarget:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TagTarget value: {data!r}")
    return cast(TagTarget, data)
