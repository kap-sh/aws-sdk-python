"""Generated from Smithy shape ``com.amazonaws.workmail#AvailabilityProviderType``."""

from typing import Literal, TypeAlias, cast

AvailabilityProviderType: TypeAlias = Literal[
    "EWS",
    "LAMBDA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityProviderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AvailabilityProviderType:
    return cast(AvailabilityProviderType, data)
