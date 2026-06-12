"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#AuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotdeviceadvisor.errors import DeserializationError

AuthenticationMethod: TypeAlias = Literal[
    "X509ClientCertificate",
    "SignatureVersion4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "X509ClientCertificate",
        "SignatureVersion4",
    )
)


def serialize_json(value: AuthenticationMethod) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationMethod value: {data!r}")
    return cast(AuthenticationMethod, data)
