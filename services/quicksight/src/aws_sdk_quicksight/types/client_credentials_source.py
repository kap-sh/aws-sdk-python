"""Generated from Smithy shape ``com.amazonaws.quicksight#ClientCredentialsSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ClientCredentialsSource: TypeAlias = Literal["PLAIN_CREDENTIALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PLAIN_CREDENTIALS",))


def serialize_json(value: ClientCredentialsSource) -> str:
    return value


def deserialize_json(data: str) -> ClientCredentialsSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClientCredentialsSource value: {data!r}")
    return cast(ClientCredentialsSource, data)
