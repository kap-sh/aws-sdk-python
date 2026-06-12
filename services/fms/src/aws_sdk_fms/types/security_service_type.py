"""Generated from Smithy shape ``com.amazonaws.fms#SecurityServiceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

SecurityServiceType: TypeAlias = Literal[
    "WAF",
    "WAFV2",
    "SHIELD_ADVANCED",
    "SECURITY_GROUPS_COMMON",
    "SECURITY_GROUPS_CONTENT_AUDIT",
    "SECURITY_GROUPS_USAGE_AUDIT",
    "NETWORK_FIREWALL",
    "DNS_FIREWALL",
    "THIRD_PARTY_FIREWALL",
    "IMPORT_NETWORK_FIREWALL",
    "NETWORK_ACL_COMMON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WAF",
        "WAFV2",
        "SHIELD_ADVANCED",
        "SECURITY_GROUPS_COMMON",
        "SECURITY_GROUPS_CONTENT_AUDIT",
        "SECURITY_GROUPS_USAGE_AUDIT",
        "NETWORK_FIREWALL",
        "DNS_FIREWALL",
        "THIRD_PARTY_FIREWALL",
        "IMPORT_NETWORK_FIREWALL",
        "NETWORK_ACL_COMMON",
    )
)


def serialize_aws_json_1_1(value: SecurityServiceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SecurityServiceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SecurityServiceType value: {data!r}")
    return cast(SecurityServiceType, data)
