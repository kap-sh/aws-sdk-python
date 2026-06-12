"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#ChecksumType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_edge.errors import DeserializationError

ChecksumType: TypeAlias = Literal["SHA1",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SHA1",))


def serialize_json(value: ChecksumType) -> str:
    return value


def deserialize_json(data: str) -> ChecksumType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChecksumType value: {data!r}")
    return cast(ChecksumType, data)
