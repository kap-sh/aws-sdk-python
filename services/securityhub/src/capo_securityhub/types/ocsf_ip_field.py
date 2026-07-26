"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfIpField``."""

from typing import Literal, TypeAlias, cast

OcsfIpField: TypeAlias = Literal[
    "evidences.dst_endpoint.ip",
    "evidences.src_endpoint.ip",
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfIpField) -> str:
    return value


def deserialize_json(data: str) -> OcsfIpField:
    return cast(OcsfIpField, data)
