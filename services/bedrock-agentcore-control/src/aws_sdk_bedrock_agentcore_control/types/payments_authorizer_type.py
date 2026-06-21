"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentsAuthorizerType``."""

from typing import Literal, TypeAlias, cast

PaymentsAuthorizerType: TypeAlias = Literal[
    "CUSTOM_JWT",
    "AWS_IAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentsAuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> PaymentsAuthorizerType:
    return cast(PaymentsAuthorizerType, data)
