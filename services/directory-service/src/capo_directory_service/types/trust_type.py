"""Generated from Smithy shape ``com.amazonaws.directoryservice#TrustType``."""

from typing import Literal, TypeAlias, cast

TrustType: TypeAlias = Literal[
    "Forest",
    "External",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrustType:
    return cast(TrustType, data)
