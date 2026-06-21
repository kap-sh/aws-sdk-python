"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DestinationType``."""

from typing import Literal, TypeAlias, cast

DestinationType: TypeAlias = Literal[
    "EVENT_DATA_STORE",
    "AWS_SERVICE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DestinationType:
    return cast(DestinationType, data)
