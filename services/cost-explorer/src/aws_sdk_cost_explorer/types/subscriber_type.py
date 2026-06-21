"""Generated from Smithy shape ``com.amazonaws.costexplorer#SubscriberType``."""

from typing import Literal, TypeAlias, cast

SubscriberType: TypeAlias = Literal[
    "EMAIL",
    "SNS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriberType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubscriberType:
    return cast(SubscriberType, data)
