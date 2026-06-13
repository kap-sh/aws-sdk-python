"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseWalletFile``."""

import base64
from typing import TypeAlias

AutonomousDatabaseWalletFile: TypeAlias = bytes


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseWalletFile) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_0(data: str) -> AutonomousDatabaseWalletFile:
    return base64.b64decode(data)
