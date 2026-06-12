"""Generated from Smithy shape ``com.amazonaws.fms#ThirdPartyFirewall``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

ThirdPartyFirewall: TypeAlias = Literal[
    "PALO_ALTO_NETWORKS_CLOUD_NGFW",
    "FORTIGATE_CLOUD_NATIVE_FIREWALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PALO_ALTO_NETWORKS_CLOUD_NGFW",
        "FORTIGATE_CLOUD_NATIVE_FIREWALL",
    )
)


def serialize_aws_json_1_1(value: ThirdPartyFirewall) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThirdPartyFirewall:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThirdPartyFirewall value: {data!r}")
    return cast(ThirdPartyFirewall, data)
