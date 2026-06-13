"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceProfileStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

InferenceProfileStatus: TypeAlias = Literal["ACTIVE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACTIVE",))


def serialize_json(value: InferenceProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> InferenceProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferenceProfileStatus value: {data!r}")
    return cast(InferenceProfileStatus, data)
