"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#AuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

AuthenticationMethod: TypeAlias = Literal[
    "X509ClientCertificate",
    "SignatureVersion4",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationMethod) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationMethod:
    return cast(AuthenticationMethod, data)
