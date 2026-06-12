"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#EncryptionOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

EncryptionOption: TypeAlias = Literal[
    "AWS_OWNED_CMK",
    "CUSTOMER_MANAGED_CMK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OWNED_CMK",
        "CUSTOMER_MANAGED_CMK",
    )
)


def serialize_json(value: EncryptionOption) -> str:
    return value


def deserialize_json(data: str) -> EncryptionOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionOption value: {data!r}")
    return cast(EncryptionOption, data)
