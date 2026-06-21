"""Generated from Smithy shape ``com.amazonaws.devicefarm#OfferingType``."""

from typing import Literal, TypeAlias, cast

OfferingType: TypeAlias = Literal["RECURRING",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfferingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OfferingType:
    return cast(OfferingType, data)
