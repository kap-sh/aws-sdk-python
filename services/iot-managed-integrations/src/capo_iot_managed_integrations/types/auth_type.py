"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AuthType``."""

from typing import Literal, TypeAlias, cast

AuthType: TypeAlias = Literal["OAUTH",]


# --- restJson1 ser/de ---
def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    return cast(AuthType, data)
