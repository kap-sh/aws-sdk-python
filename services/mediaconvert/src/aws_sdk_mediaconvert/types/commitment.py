"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Commitment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""The length of the term of your reserved queue pricing plan commitment."""
Commitment: TypeAlias = Literal["ONE_YEAR",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ONE_YEAR",))


def serialize_json(value: Commitment) -> str:
    return value


def deserialize_json(data: str) -> Commitment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Commitment value: {data!r}")
    return cast(Commitment, data)
