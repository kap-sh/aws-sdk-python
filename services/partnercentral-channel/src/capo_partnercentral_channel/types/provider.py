"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#Provider``."""

from typing import Literal, TypeAlias, cast

Provider: TypeAlias = Literal[
    "DISTRIBUTOR",
    "DISTRIBUTION_SELLER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Provider) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Provider:
    return cast(Provider, data)
