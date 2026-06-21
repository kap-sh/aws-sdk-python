"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateDnsRecordCreationStateCode``."""

from typing import Literal, TypeAlias, cast

LoadBalancerTlsCertificateDnsRecordCreationStateCode: TypeAlias = Literal[
    "SUCCEEDED",
    "STARTED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: LoadBalancerTlsCertificateDnsRecordCreationStateCode,
) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> LoadBalancerTlsCertificateDnsRecordCreationStateCode:
    return cast(LoadBalancerTlsCertificateDnsRecordCreationStateCode, data)
