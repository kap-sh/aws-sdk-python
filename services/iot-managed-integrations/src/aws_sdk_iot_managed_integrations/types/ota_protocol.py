"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaProtocol``."""

from typing import Literal, TypeAlias, cast

OtaProtocol: TypeAlias = Literal["HTTP",]


# --- restJson1 ser/de ---
def serialize_json(value: OtaProtocol) -> str:
    return value


def deserialize_json(data: str) -> OtaProtocol:
    return cast(OtaProtocol, data)
