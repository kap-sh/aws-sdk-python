"""Generated from Smithy shape ``com.amazonaws.storagegateway#SMBSecurityStrategy``."""

from typing import Literal, TypeAlias, cast

SMBSecurityStrategy: TypeAlias = Literal[
    "ClientSpecified",
    "MandatorySigning",
    "MandatoryEncryption",
    "MandatoryEncryptionNoAes128",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SMBSecurityStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SMBSecurityStrategy:
    return cast(SMBSecurityStrategy, data)
