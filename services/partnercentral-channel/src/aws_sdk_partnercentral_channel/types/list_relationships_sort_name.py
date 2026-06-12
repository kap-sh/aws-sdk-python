"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListRelationshipsSortName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

ListRelationshipsSortName: TypeAlias = Literal["UpdatedAt",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("UpdatedAt",))


def serialize_aws_json_1_0(value: ListRelationshipsSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListRelationshipsSortName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListRelationshipsSortName value: {data!r}")
    return cast(ListRelationshipsSortName, data)
