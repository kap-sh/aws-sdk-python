"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#MarketingSource``."""

from typing import Literal, TypeAlias, cast

MarketingSource: TypeAlias = Literal[
    "Marketing Activity",
    "None",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MarketingSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MarketingSource:
    return cast(MarketingSource, data)
