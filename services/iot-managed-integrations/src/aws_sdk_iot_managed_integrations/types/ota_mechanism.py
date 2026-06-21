"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaMechanism``."""

from typing import Literal, TypeAlias, cast

OtaMechanism: TypeAlias = Literal["PUSH",]


# --- restJson1 ser/de ---
def serialize_json(value: OtaMechanism) -> str:
    return value


def deserialize_json(data: str) -> OtaMechanism:
    return cast(OtaMechanism, data)
