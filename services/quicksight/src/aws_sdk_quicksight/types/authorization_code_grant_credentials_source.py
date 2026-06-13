"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizationCodeGrantCredentialsSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AuthorizationCodeGrantCredentialsSource: TypeAlias = Literal["PLAIN_CREDENTIALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PLAIN_CREDENTIALS",))


def serialize_json(value: AuthorizationCodeGrantCredentialsSource) -> str:
    return value


def deserialize_json(data: str) -> AuthorizationCodeGrantCredentialsSource:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AuthorizationCodeGrantCredentialsSource value: {data!r}"
        )
    return cast(AuthorizationCodeGrantCredentialsSource, data)
