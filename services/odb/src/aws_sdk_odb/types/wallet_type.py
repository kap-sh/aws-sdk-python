"""Generated from Smithy shape ``com.amazonaws.odb#WalletType``."""

from typing import Literal, TypeAlias, cast

WalletType: TypeAlias = Literal[
    "REGIONAL",
    "INSTANCE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WalletType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WalletType:
    return cast(WalletType, data)
