"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateDnsRecordCreationStateCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

LoadBalancerTlsCertificateDnsRecordCreationStateCode: TypeAlias = Literal[
    "SUCCEEDED",
    "STARTED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "STARTED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(
    value: LoadBalancerTlsCertificateDnsRecordCreationStateCode,
) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> LoadBalancerTlsCertificateDnsRecordCreationStateCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LoadBalancerTlsCertificateDnsRecordCreationStateCode value: {data!r}"
        )
    return cast(LoadBalancerTlsCertificateDnsRecordCreationStateCode, data)
