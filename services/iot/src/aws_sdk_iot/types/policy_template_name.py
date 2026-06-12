"""Generated from Smithy shape ``com.amazonaws.iot#PolicyTemplateName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

PolicyTemplateName: TypeAlias = Literal["BLANK_POLICY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BLANK_POLICY",))


def serialize_json(value: PolicyTemplateName) -> str:
    return value


def deserialize_json(data: str) -> PolicyTemplateName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyTemplateName value: {data!r}")
    return cast(PolicyTemplateName, data)
