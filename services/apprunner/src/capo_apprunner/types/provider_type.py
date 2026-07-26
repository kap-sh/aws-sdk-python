"""Generated from Smithy shape ``com.amazonaws.apprunner#ProviderType``."""

from typing import Literal, TypeAlias, cast

ProviderType: TypeAlias = Literal[
    "GITHUB",
    "BITBUCKET",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProviderType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProviderType:
    return cast(ProviderType, data)
