"""Generated from Smithy shape ``com.amazonaws.lightsail#AccountLevelBpaSyncStatus``."""

from typing import Literal, TypeAlias, cast

AccountLevelBpaSyncStatus: TypeAlias = Literal[
    "InSync",
    "Failed",
    "NeverSynced",
    "Defaulted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountLevelBpaSyncStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountLevelBpaSyncStatus:
    return cast(AccountLevelBpaSyncStatus, data)
