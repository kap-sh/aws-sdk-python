"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceChatterFeedIncludeFilterType``."""

from typing import Literal, TypeAlias, cast

SalesforceChatterFeedIncludeFilterType: TypeAlias = Literal[
    "ACTIVE_USER",
    "STANDARD_USER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceChatterFeedIncludeFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SalesforceChatterFeedIncludeFilterType:
    return cast(SalesforceChatterFeedIncludeFilterType, data)
