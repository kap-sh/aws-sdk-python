"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListProgramManagementAccountsSortName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

ListProgramManagementAccountsSortName: TypeAlias = Literal["UpdatedAt",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("UpdatedAt",))


def serialize_aws_json_1_0(value: ListProgramManagementAccountsSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListProgramManagementAccountsSortName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListProgramManagementAccountsSortName value: {data!r}"
        )
    return cast(ListProgramManagementAccountsSortName, data)
