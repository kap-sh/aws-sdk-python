"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

SortBy: TypeAlias = Literal["CreatedDate",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CreatedDate",))


def serialize_aws_json_1_0(value: SortBy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortBy value: {data!r}")
    return cast(SortBy, data)
