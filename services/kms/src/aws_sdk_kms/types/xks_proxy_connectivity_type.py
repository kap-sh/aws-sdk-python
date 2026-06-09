"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyConnectivityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

XksProxyConnectivityType: TypeAlias = Literal[
    "PUBLIC_ENDPOINT",
    "VPC_ENDPOINT_SERVICE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC_ENDPOINT",
        "VPC_ENDPOINT_SERVICE",
    )
)


def serialize_aws_json_1_1(value: XksProxyConnectivityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> XksProxyConnectivityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown XksProxyConnectivityType value: {data!r}")
    return cast(XksProxyConnectivityType, data)
