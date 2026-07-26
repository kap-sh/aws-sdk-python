"""Generated from Smithy shape ``com.amazonaws.transfer#EnforceMessageSigningType``."""

from typing import Literal, TypeAlias, cast

EnforceMessageSigningType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnforceMessageSigningType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnforceMessageSigningType:
    return cast(EnforceMessageSigningType, data)
