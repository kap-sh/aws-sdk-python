"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#EncryptionOption``."""

from typing import Literal, TypeAlias, cast

EncryptionOption: TypeAlias = Literal[
    "AWS_OWNED_CMK",
    "CUSTOMER_MANAGED_CMK",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionOption) -> str:
    return value


def deserialize_json(data: str) -> EncryptionOption:
    return cast(EncryptionOption, data)
