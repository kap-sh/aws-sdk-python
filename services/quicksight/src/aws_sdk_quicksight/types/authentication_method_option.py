"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthenticationMethodOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AuthenticationMethodOption: TypeAlias = Literal[
    "IAM_AND_QUICKSIGHT",
    "IAM_ONLY",
    "ACTIVE_DIRECTORY",
    "IAM_IDENTITY_CENTER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM_AND_QUICKSIGHT",
        "IAM_ONLY",
        "ACTIVE_DIRECTORY",
        "IAM_IDENTITY_CENTER",
    )
)


def serialize_json(value: AuthenticationMethodOption) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationMethodOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AuthenticationMethodOption value: {data!r}"
        )
    return cast(AuthenticationMethodOption, data)
