"""Generated from Smithy shape ``com.amazonaws.configservice#DeliveryStatus``."""

from typing import Literal, TypeAlias, cast

DeliveryStatus: TypeAlias = Literal[
    "Success",
    "Failure",
    "Not_Applicable",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStatus:
    return cast(DeliveryStatus, data)
