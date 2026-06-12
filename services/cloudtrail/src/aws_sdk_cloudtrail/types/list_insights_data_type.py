"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListInsightsDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

ListInsightsDataType: TypeAlias = Literal["InsightsEvents",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("InsightsEvents",))


def serialize_aws_json_1_1(value: ListInsightsDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListInsightsDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListInsightsDataType value: {data!r}")
    return cast(ListInsightsDataType, data)
