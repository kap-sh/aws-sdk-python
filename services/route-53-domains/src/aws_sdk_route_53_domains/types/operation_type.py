"""Generated from Smithy shape ``com.amazonaws.route53domains#OperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53_domains.errors import DeserializationError

OperationType: TypeAlias = Literal[
    "REGISTER_DOMAIN",
    "DELETE_DOMAIN",
    "TRANSFER_IN_DOMAIN",
    "UPDATE_DOMAIN_CONTACT",
    "UPDATE_NAMESERVER",
    "CHANGE_PRIVACY_PROTECTION",
    "DOMAIN_LOCK",
    "ENABLE_AUTORENEW",
    "DISABLE_AUTORENEW",
    "ADD_DNSSEC",
    "REMOVE_DNSSEC",
    "EXPIRE_DOMAIN",
    "TRANSFER_OUT_DOMAIN",
    "CHANGE_DOMAIN_OWNER",
    "RENEW_DOMAIN",
    "PUSH_DOMAIN",
    "INTERNAL_TRANSFER_OUT_DOMAIN",
    "INTERNAL_TRANSFER_IN_DOMAIN",
    "RELEASE_TO_GANDI",
    "TRANSFER_ON_RENEW",
    "RESTORE_DOMAIN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGISTER_DOMAIN",
        "DELETE_DOMAIN",
        "TRANSFER_IN_DOMAIN",
        "UPDATE_DOMAIN_CONTACT",
        "UPDATE_NAMESERVER",
        "CHANGE_PRIVACY_PROTECTION",
        "DOMAIN_LOCK",
        "ENABLE_AUTORENEW",
        "DISABLE_AUTORENEW",
        "ADD_DNSSEC",
        "REMOVE_DNSSEC",
        "EXPIRE_DOMAIN",
        "TRANSFER_OUT_DOMAIN",
        "CHANGE_DOMAIN_OWNER",
        "RENEW_DOMAIN",
        "PUSH_DOMAIN",
        "INTERNAL_TRANSFER_OUT_DOMAIN",
        "INTERNAL_TRANSFER_IN_DOMAIN",
        "RELEASE_TO_GANDI",
        "TRANSFER_ON_RENEW",
        "RESTORE_DOMAIN",
    )
)


def serialize_aws_json_1_1(value: OperationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationType value: {data!r}")
    return cast(OperationType, data)
