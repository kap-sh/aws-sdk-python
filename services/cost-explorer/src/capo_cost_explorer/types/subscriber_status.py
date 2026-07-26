"""Generated from Smithy shape ``com.amazonaws.costexplorer#SubscriberStatus``."""

from typing import Literal, TypeAlias, cast

SubscriberStatus: TypeAlias = Literal[
    "CONFIRMED",
    "DECLINED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriberStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubscriberStatus:
    return cast(SubscriberStatus, data)
