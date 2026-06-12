"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListTasksSortName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

ListTasksSortName: TypeAlias = Literal["StartTime",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("StartTime",))


def serialize_aws_json_1_0(value: ListTasksSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListTasksSortName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListTasksSortName value: {data!r}")
    return cast(ListTasksSortName, data)
