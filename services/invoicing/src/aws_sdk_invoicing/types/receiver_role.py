"""Generated from Smithy shape ``com.amazonaws.invoicing#ReceiverRole``."""

from typing import Literal, TypeAlias, cast

ReceiverRole: TypeAlias = Literal[
    "SELLER",
    "RESELLER",
    "BUYER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReceiverRole) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReceiverRole:
    return cast(ReceiverRole, data)
