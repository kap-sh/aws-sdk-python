"""Generated from Smithy shape ``com.amazonaws.securityhub#ThreatIntelIndicatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ThreatIntelIndicatorType: TypeAlias = Literal[
    "DOMAIN",
    "EMAIL_ADDRESS",
    "HASH_MD5",
    "HASH_SHA1",
    "HASH_SHA256",
    "HASH_SHA512",
    "IPV4_ADDRESS",
    "IPV6_ADDRESS",
    "MUTEX",
    "PROCESS",
    "URL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOMAIN",
        "EMAIL_ADDRESS",
        "HASH_MD5",
        "HASH_SHA1",
        "HASH_SHA256",
        "HASH_SHA512",
        "IPV4_ADDRESS",
        "IPV6_ADDRESS",
        "MUTEX",
        "PROCESS",
        "URL",
    )
)


def serialize_json(value: ThreatIntelIndicatorType) -> str:
    return value


def deserialize_json(data: str) -> ThreatIntelIndicatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThreatIntelIndicatorType value: {data!r}")
    return cast(ThreatIntelIndicatorType, data)
