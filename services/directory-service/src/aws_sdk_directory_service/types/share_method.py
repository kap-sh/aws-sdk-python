"""Generated from Smithy shape ``com.amazonaws.directoryservice#ShareMethod``."""

from typing import Literal, TypeAlias, cast

ShareMethod: TypeAlias = Literal[
    "ORGANIZATIONS",
    "HANDSHAKE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShareMethod:
    return cast(ShareMethod, data)
