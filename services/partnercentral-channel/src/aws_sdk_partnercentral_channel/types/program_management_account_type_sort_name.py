"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountTypeSortName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

ProgramManagementAccountTypeSortName: TypeAlias = Literal["UpdatedAt",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("UpdatedAt",))


def serialize_aws_json_1_0(value: ProgramManagementAccountTypeSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProgramManagementAccountTypeSortName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProgramManagementAccountTypeSortName value: {data!r}"
        )
    return cast(ProgramManagementAccountTypeSortName, data)
