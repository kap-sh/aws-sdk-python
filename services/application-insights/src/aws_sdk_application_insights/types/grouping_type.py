"""Generated from Smithy shape ``com.amazonaws.applicationinsights#GroupingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

GroupingType: TypeAlias = Literal["ACCOUNT_BASED",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACCOUNT_BASED",))


def serialize_aws_json_1_1(value: GroupingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GroupingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupingType value: {data!r}")
    return cast(GroupingType, data)
