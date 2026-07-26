"""Generated from Smithy shape ``com.amazonaws.costexplorer#OfferingClass``."""

from typing import Literal, TypeAlias, cast

OfferingClass: TypeAlias = Literal[
    "STANDARD",
    "CONVERTIBLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfferingClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OfferingClass:
    return cast(OfferingClass, data)
