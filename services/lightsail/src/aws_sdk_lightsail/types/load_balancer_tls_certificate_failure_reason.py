"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateFailureReason``."""

from typing import Literal, TypeAlias, cast

LoadBalancerTlsCertificateFailureReason: TypeAlias = Literal[
    "NO_AVAILABLE_CONTACTS",
    "ADDITIONAL_VERIFICATION_REQUIRED",
    "DOMAIN_NOT_ALLOWED",
    "INVALID_PUBLIC_DOMAIN",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateFailureReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerTlsCertificateFailureReason:
    return cast(LoadBalancerTlsCertificateFailureReason, data)
