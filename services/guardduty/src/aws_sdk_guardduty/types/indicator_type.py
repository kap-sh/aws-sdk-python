"""Generated from Smithy shape ``com.amazonaws.guardduty#IndicatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

IndicatorType: TypeAlias = Literal[
    "SUSPICIOUS_USER_AGENT",
    "SUSPICIOUS_NETWORK",
    "MALICIOUS_IP",
    "TOR_IP",
    "ATTACK_TACTIC",
    "HIGH_RISK_API",
    "ATTACK_TECHNIQUE",
    "UNUSUAL_API_FOR_ACCOUNT",
    "UNUSUAL_ASN_FOR_ACCOUNT",
    "UNUSUAL_ASN_FOR_USER",
    "SUSPICIOUS_PROCESS",
    "MALICIOUS_DOMAIN",
    "MALICIOUS_PROCESS",
    "CRYPTOMINING_IP",
    "CRYPTOMINING_DOMAIN",
    "CRYPTOMINING_PROCESS",
    "MALICIOUS_FILE",
    "VULNERABILITY",
    "MALICIOUS_PACKAGE",
    "MISCONFIGURATION",
    "REACHABILITY",
    "SENSITIVE_DATA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUSPICIOUS_USER_AGENT",
        "SUSPICIOUS_NETWORK",
        "MALICIOUS_IP",
        "TOR_IP",
        "ATTACK_TACTIC",
        "HIGH_RISK_API",
        "ATTACK_TECHNIQUE",
        "UNUSUAL_API_FOR_ACCOUNT",
        "UNUSUAL_ASN_FOR_ACCOUNT",
        "UNUSUAL_ASN_FOR_USER",
        "SUSPICIOUS_PROCESS",
        "MALICIOUS_DOMAIN",
        "MALICIOUS_PROCESS",
        "CRYPTOMINING_IP",
        "CRYPTOMINING_DOMAIN",
        "CRYPTOMINING_PROCESS",
        "MALICIOUS_FILE",
        "VULNERABILITY",
        "MALICIOUS_PACKAGE",
        "MISCONFIGURATION",
        "REACHABILITY",
        "SENSITIVE_DATA",
    )
)


def serialize_json(value: IndicatorType) -> str:
    return value


def deserialize_json(data: str) -> IndicatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IndicatorType value: {data!r}")
    return cast(IndicatorType, data)
