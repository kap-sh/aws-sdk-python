"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseWalletStatus``."""

from typing import Literal, TypeAlias, cast

AutonomousDatabaseWalletStatus: TypeAlias = Literal[
    "ACTIVE",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseWalletStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutonomousDatabaseWalletStatus:
    return cast(AutonomousDatabaseWalletStatus, data)
