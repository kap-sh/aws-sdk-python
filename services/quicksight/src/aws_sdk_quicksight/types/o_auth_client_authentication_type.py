"""Generated from Smithy shape ``com.amazonaws.quicksight#OAuthClientAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

OAuthClientAuthenticationType: TypeAlias = Literal["TOKEN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TOKEN",))


def serialize_json(value: OAuthClientAuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> OAuthClientAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OAuthClientAuthenticationType value: {data!r}"
        )
    return cast(OAuthClientAuthenticationType, data)
