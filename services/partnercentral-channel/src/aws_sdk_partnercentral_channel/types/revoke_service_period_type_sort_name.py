"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RevokeServicePeriodTypeSortName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

RevokeServicePeriodTypeSortName: TypeAlias = Literal["UpdatedAt",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("UpdatedAt",))


def serialize_aws_json_1_0(value: RevokeServicePeriodTypeSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RevokeServicePeriodTypeSortName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RevokeServicePeriodTypeSortName value: {data!r}"
        )
    return cast(RevokeServicePeriodTypeSortName, data)
