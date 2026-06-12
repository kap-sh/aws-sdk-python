"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

LoadBalancerTlsCertificateStatus: TypeAlias = Literal[
    "PENDING_VALIDATION",
    "ISSUED",
    "INACTIVE",
    "EXPIRED",
    "VALIDATION_TIMED_OUT",
    "REVOKED",
    "FAILED",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_VALIDATION",
        "ISSUED",
        "INACTIVE",
        "EXPIRED",
        "VALIDATION_TIMED_OUT",
        "REVOKED",
        "FAILED",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerTlsCertificateStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LoadBalancerTlsCertificateStatus value: {data!r}"
        )
    return cast(LoadBalancerTlsCertificateStatus, data)
