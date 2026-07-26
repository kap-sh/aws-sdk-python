"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerTlsCertificateStatus:
    return cast(LoadBalancerTlsCertificateStatus, data)
