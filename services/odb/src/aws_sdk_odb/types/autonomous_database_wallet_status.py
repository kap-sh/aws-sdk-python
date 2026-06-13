"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseWalletStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

AutonomousDatabaseWalletStatus: TypeAlias = Literal[
    "ACTIVE",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "UPDATING",
    )
)


def serialize_aws_json_1_0(value: AutonomousDatabaseWalletStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutonomousDatabaseWalletStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutonomousDatabaseWalletStatus value: {data!r}"
        )
    return cast(AutonomousDatabaseWalletStatus, data)
