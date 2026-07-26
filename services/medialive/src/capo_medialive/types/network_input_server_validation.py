"""Generated from Smithy shape ``com.amazonaws.medialive#NetworkInputServerValidation``."""

from typing import Literal, TypeAlias, cast

"""Network Input Server Validation"""
NetworkInputServerValidation: TypeAlias = Literal[
    "CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME",
    "CHECK_CRYPTOGRAPHY_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInputServerValidation) -> str:
    return value


def deserialize_json(data: str) -> NetworkInputServerValidation:
    return cast(NetworkInputServerValidation, data)
