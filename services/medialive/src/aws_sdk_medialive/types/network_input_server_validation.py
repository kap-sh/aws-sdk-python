"""Generated from Smithy shape ``com.amazonaws.medialive#NetworkInputServerValidation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Network Input Server Validation"""
NetworkInputServerValidation: TypeAlias = Literal[
    "CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME",
    "CHECK_CRYPTOGRAPHY_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME",
        "CHECK_CRYPTOGRAPHY_ONLY",
    )
)


def serialize_json(value: NetworkInputServerValidation) -> str:
    return value


def deserialize_json(data: str) -> NetworkInputServerValidation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NetworkInputServerValidation value: {data!r}"
        )
    return cast(NetworkInputServerValidation, data)
