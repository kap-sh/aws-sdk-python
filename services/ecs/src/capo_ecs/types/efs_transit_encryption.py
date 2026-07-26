"""Generated from Smithy shape ``com.amazonaws.ecs#EFSTransitEncryption``."""

from typing import Literal, TypeAlias, cast

EFSTransitEncryption: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EFSTransitEncryption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EFSTransitEncryption:
    return cast(EFSTransitEncryption, data)
