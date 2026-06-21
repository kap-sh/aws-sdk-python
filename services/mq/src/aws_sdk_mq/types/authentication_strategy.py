"""Generated from Smithy shape ``com.amazonaws.mq#AuthenticationStrategy``."""

from typing import Literal, TypeAlias, cast

"""<p>Optional. The authentication strategy used to secure the broker. The default is SIMPLE.</p>"""
AuthenticationStrategy: TypeAlias = Literal[
    "SIMPLE",
    "LDAP",
    "CONFIG_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationStrategy) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationStrategy:
    return cast(AuthenticationStrategy, data)
