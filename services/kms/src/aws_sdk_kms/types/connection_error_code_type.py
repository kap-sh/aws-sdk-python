"""Generated from Smithy shape ``com.amazonaws.kms#ConnectionErrorCodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

ConnectionErrorCodeType: TypeAlias = Literal[
    "INVALID_CREDENTIALS",
    "CLUSTER_NOT_FOUND",
    "NETWORK_ERRORS",
    "INTERNAL_ERROR",
    "INSUFFICIENT_CLOUDHSM_HSMS",
    "USER_LOCKED_OUT",
    "USER_NOT_FOUND",
    "USER_LOGGED_IN",
    "SUBNET_NOT_FOUND",
    "INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET",
    "XKS_PROXY_ACCESS_DENIED",
    "XKS_PROXY_NOT_REACHABLE",
    "XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND",
    "XKS_PROXY_INVALID_RESPONSE",
    "XKS_PROXY_INVALID_CONFIGURATION",
    "XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION",
    "XKS_PROXY_TIMED_OUT",
    "XKS_PROXY_INVALID_TLS_CONFIGURATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_CREDENTIALS",
        "CLUSTER_NOT_FOUND",
        "NETWORK_ERRORS",
        "INTERNAL_ERROR",
        "INSUFFICIENT_CLOUDHSM_HSMS",
        "USER_LOCKED_OUT",
        "USER_NOT_FOUND",
        "USER_LOGGED_IN",
        "SUBNET_NOT_FOUND",
        "INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET",
        "XKS_PROXY_ACCESS_DENIED",
        "XKS_PROXY_NOT_REACHABLE",
        "XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND",
        "XKS_PROXY_INVALID_RESPONSE",
        "XKS_PROXY_INVALID_CONFIGURATION",
        "XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION",
        "XKS_PROXY_TIMED_OUT",
        "XKS_PROXY_INVALID_TLS_CONFIGURATION",
    )
)


def serialize_aws_json_1_1(value: ConnectionErrorCodeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionErrorCodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionErrorCodeType value: {data!r}")
    return cast(ConnectionErrorCodeType, data)
