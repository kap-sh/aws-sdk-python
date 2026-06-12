"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

ProgramManagementAccountStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_0(value: ProgramManagementAccountStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProgramManagementAccountStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProgramManagementAccountStatus value: {data!r}"
        )
    return cast(ProgramManagementAccountStatus, data)
