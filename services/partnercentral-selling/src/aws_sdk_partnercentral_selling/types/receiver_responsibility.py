"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ReceiverResponsibility``."""

from typing import Literal, TypeAlias, cast

ReceiverResponsibility: TypeAlias = Literal[
    "Distributor",
    "Reseller",
    "Hardware Partner",
    "Managed Service Provider",
    "Software Partner",
    "Services Partner",
    "Training Partner",
    "Co-Sell Facilitator",
    "Facilitator",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReceiverResponsibility) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReceiverResponsibility:
    return cast(ReceiverResponsibility, data)
