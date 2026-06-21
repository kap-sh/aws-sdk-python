"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateRenewalStatus``."""

from typing import Literal, TypeAlias, cast

LoadBalancerTlsCertificateRenewalStatus: TypeAlias = Literal[
    "PENDING_AUTO_RENEWAL",
    "PENDING_VALIDATION",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateRenewalStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerTlsCertificateRenewalStatus:
    return cast(LoadBalancerTlsCertificateRenewalStatus, data)
