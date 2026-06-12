"""Generated from Smithy shape ``com.amazonaws.networkfirewall#GeneratedRulesType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

GeneratedRulesType: TypeAlias = Literal[
    "ALLOWLIST",
    "DENYLIST",
    "REJECTLIST",
    "ALERTLIST",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOWLIST",
        "DENYLIST",
        "REJECTLIST",
        "ALERTLIST",
    )
)


def serialize_aws_json_1_0(value: GeneratedRulesType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GeneratedRulesType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeneratedRulesType value: {data!r}")
    return cast(GeneratedRulesType, data)
