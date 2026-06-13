"""Generated from Smithy shape ``com.amazonaws.securityagent#ProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Type of provider integration.</p>"""
ProviderType: TypeAlias = Literal[
    "SOURCE_CODE",
    "DOCUMENTATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOURCE_CODE",
        "DOCUMENTATION",
    )
)


def serialize_json(value: ProviderType) -> str:
    return value


def deserialize_json(data: str) -> ProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProviderType value: {data!r}")
    return cast(ProviderType, data)
