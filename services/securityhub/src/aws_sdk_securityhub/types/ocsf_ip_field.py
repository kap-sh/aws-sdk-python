"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfIpField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

OcsfIpField: TypeAlias = Literal[
    "evidences.dst_endpoint.ip",
    "evidences.src_endpoint.ip",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "evidences.dst_endpoint.ip",
        "evidences.src_endpoint.ip",
    )
)


def serialize_json(value: OcsfIpField) -> str:
    return value


def deserialize_json(data: str) -> OcsfIpField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OcsfIpField value: {data!r}")
    return cast(OcsfIpField, data)
