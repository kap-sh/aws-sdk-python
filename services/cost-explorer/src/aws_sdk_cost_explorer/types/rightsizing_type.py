"""Generated from Smithy shape ``com.amazonaws.costexplorer#RightsizingType``."""

from typing import Literal, TypeAlias, cast

RightsizingType: TypeAlias = Literal[
    "TERMINATE",
    "MODIFY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RightsizingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RightsizingType:
    return cast(RightsizingType, data)
