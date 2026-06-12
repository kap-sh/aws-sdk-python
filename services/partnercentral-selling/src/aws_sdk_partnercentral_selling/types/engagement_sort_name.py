"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementSortName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

EngagementSortName: TypeAlias = Literal["CreatedDate",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CreatedDate",))


def serialize_aws_json_1_0(value: EngagementSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EngagementSortName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EngagementSortName value: {data!r}")
    return cast(EngagementSortName, data)
