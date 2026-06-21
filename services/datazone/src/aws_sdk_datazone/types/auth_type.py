"""Generated from Smithy shape ``com.amazonaws.datazone#AuthType``."""

from typing import Literal, TypeAlias, cast

AuthType: TypeAlias = Literal[
    "IAM_IDC",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    return cast(AuthType, data)
