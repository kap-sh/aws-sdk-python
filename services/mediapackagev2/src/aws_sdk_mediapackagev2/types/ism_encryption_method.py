"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#IsmEncryptionMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

IsmEncryptionMethod: TypeAlias = Literal["CENC",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CENC",))


def serialize_json(value: IsmEncryptionMethod) -> str:
    return value


def deserialize_json(data: str) -> IsmEncryptionMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsmEncryptionMethod value: {data!r}")
    return cast(IsmEncryptionMethod, data)
