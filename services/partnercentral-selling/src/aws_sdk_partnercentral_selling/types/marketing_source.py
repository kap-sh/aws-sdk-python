"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#MarketingSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

MarketingSource: TypeAlias = Literal[
    "Marketing Activity",
    "None",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Marketing Activity",
        "None",
    )
)


def serialize_aws_json_1_0(value: MarketingSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MarketingSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MarketingSource value: {data!r}")
    return cast(MarketingSource, data)
