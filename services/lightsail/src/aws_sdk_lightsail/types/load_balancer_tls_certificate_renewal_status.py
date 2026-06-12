"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateRenewalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

LoadBalancerTlsCertificateRenewalStatus: TypeAlias = Literal[
    "PENDING_AUTO_RENEWAL",
    "PENDING_VALIDATION",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_AUTO_RENEWAL",
        "PENDING_VALIDATION",
        "SUCCESS",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateRenewalStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerTlsCertificateRenewalStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LoadBalancerTlsCertificateRenewalStatus value: {data!r}"
        )
    return cast(LoadBalancerTlsCertificateRenewalStatus, data)
