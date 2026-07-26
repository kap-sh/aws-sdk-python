"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#InheritedProperty``."""

from typing import Literal, TypeAlias, cast

InheritedProperty: TypeAlias = Literal["ACCOUNT_DATA_PROTECTION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InheritedProperty) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InheritedProperty:
    return cast(InheritedProperty, data)
