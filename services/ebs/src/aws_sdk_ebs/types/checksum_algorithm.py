"""Generated from Smithy shape ``com.amazonaws.ebs#ChecksumAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ebs.errors import DeserializationError

ChecksumAlgorithm: TypeAlias = Literal["SHA256",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SHA256",))


def serialize_json(value: ChecksumAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> ChecksumAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChecksumAlgorithm value: {data!r}")
    return cast(ChecksumAlgorithm, data)
