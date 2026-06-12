"""Generated from Smithy shape ``com.amazonaws.networkfirewall#EnabledAnalysisType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

EnabledAnalysisType: TypeAlias = Literal[
    "TLS_SNI",
    "HTTP_HOST",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TLS_SNI",
        "HTTP_HOST",
    )
)


def serialize_aws_json_1_0(value: EnabledAnalysisType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnabledAnalysisType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnabledAnalysisType value: {data!r}")
    return cast(EnabledAnalysisType, data)
