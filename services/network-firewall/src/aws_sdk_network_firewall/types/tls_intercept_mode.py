"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TlsInterceptMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

TlsInterceptMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: TlsInterceptMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TlsInterceptMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TlsInterceptMode value: {data!r}")
    return cast(TlsInterceptMode, data)
