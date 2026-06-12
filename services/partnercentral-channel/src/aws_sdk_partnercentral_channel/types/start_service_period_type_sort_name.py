"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#StartServicePeriodTypeSortName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

StartServicePeriodTypeSortName: TypeAlias = Literal["UpdatedAt",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("UpdatedAt",))


def serialize_aws_json_1_0(value: StartServicePeriodTypeSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StartServicePeriodTypeSortName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StartServicePeriodTypeSortName value: {data!r}"
        )
    return cast(StartServicePeriodTypeSortName, data)
