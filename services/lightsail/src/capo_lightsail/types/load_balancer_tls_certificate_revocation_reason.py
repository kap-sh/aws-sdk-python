"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateRevocationReason``."""

from typing import Literal, TypeAlias, cast

LoadBalancerTlsCertificateRevocationReason: TypeAlias = Literal[
    "UNSPECIFIED",
    "KEY_COMPROMISE",
    "CA_COMPROMISE",
    "AFFILIATION_CHANGED",
    "SUPERCEDED",
    "CESSATION_OF_OPERATION",
    "CERTIFICATE_HOLD",
    "REMOVE_FROM_CRL",
    "PRIVILEGE_WITHDRAWN",
    "A_A_COMPROMISE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateRevocationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerTlsCertificateRevocationReason:
    return cast(LoadBalancerTlsCertificateRevocationReason, data)
