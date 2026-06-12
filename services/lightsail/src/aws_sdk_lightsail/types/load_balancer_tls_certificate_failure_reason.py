"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateFailureReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

LoadBalancerTlsCertificateFailureReason: TypeAlias = Literal[
    "NO_AVAILABLE_CONTACTS",
    "ADDITIONAL_VERIFICATION_REQUIRED",
    "DOMAIN_NOT_ALLOWED",
    "INVALID_PUBLIC_DOMAIN",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_AVAILABLE_CONTACTS",
        "ADDITIONAL_VERIFICATION_REQUIRED",
        "DOMAIN_NOT_ALLOWED",
        "INVALID_PUBLIC_DOMAIN",
        "OTHER",
    )
)


def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateFailureReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerTlsCertificateFailureReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LoadBalancerTlsCertificateFailureReason value: {data!r}"
        )
    return cast(LoadBalancerTlsCertificateFailureReason, data)
