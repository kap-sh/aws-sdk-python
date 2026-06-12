"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateDomainStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

LoadBalancerTlsCertificateDomainStatus: TypeAlias = Literal[
    "PENDING_VALIDATION",
    "FAILED",
    "SUCCESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_VALIDATION",
        "FAILED",
        "SUCCESS",
    )
)


def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateDomainStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerTlsCertificateDomainStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LoadBalancerTlsCertificateDomainStatus value: {data!r}"
        )
    return cast(LoadBalancerTlsCertificateDomainStatus, data)
