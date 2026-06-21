"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DiscoveryType``."""

from typing import Literal, TypeAlias, cast

DiscoveryType: TypeAlias = Literal[
    "RESOURCE_GROUP_BASED",
    "ACCOUNT_BASED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoveryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DiscoveryType:
    return cast(DiscoveryType, data)
