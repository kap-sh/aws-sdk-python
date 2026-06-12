"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainListStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

FirewallDomainListStatus: TypeAlias = Literal[
    "COMPLETE",
    "COMPLETE_IMPORT_FAILED",
    "IMPORTING",
    "DELETING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "COMPLETE_IMPORT_FAILED",
        "IMPORTING",
        "DELETING",
        "UPDATING",
    )
)


def serialize_aws_json_1_1(value: FirewallDomainListStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallDomainListStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FirewallDomainListStatus value: {data!r}")
    return cast(FirewallDomainListStatus, data)
