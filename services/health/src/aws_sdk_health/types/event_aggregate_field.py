"""Generated from Smithy shape ``com.amazonaws.health#eventAggregateField``."""

from typing import Literal, TypeAlias, cast

eventAggregateField: TypeAlias = Literal["eventTypeCategory",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventAggregateField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> eventAggregateField:
    return cast(eventAggregateField, data)
