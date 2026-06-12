"""Generated from Smithy shape ``com.amazonaws.mq#AuthenticationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mq.errors import DeserializationError

"""<p>Optional. The authentication strategy used to secure the broker. The default is SIMPLE.</p>"""
AuthenticationStrategy: TypeAlias = Literal[
    "SIMPLE",
    "LDAP",
    "CONFIG_MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SIMPLE",
        "LDAP",
        "CONFIG_MANAGED",
    )
)


def serialize_json(value: AuthenticationStrategy) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationStrategy value: {data!r}")
    return cast(AuthenticationStrategy, data)
