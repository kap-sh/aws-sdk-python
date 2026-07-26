"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateDomainStatus``."""

from typing import Literal, TypeAlias, cast

LoadBalancerTlsCertificateDomainStatus: TypeAlias = Literal[
    "PENDING_VALIDATION",
    "FAILED",
    "SUCCESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateDomainStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerTlsCertificateDomainStatus:
    return cast(LoadBalancerTlsCertificateDomainStatus, data)
