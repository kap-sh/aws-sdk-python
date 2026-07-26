"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthenticationMethodOption``."""

from typing import Literal, TypeAlias, cast

AuthenticationMethodOption: TypeAlias = Literal[
    "IAM_AND_QUICKSIGHT",
    "IAM_ONLY",
    "ACTIVE_DIRECTORY",
    "IAM_IDENTITY_CENTER",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationMethodOption) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationMethodOption:
    return cast(AuthenticationMethodOption, data)
