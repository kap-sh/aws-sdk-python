"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PlacementConstraintType``."""

from typing import Literal, TypeAlias, cast

PlacementConstraintType: TypeAlias = Literal[
    "distinctInstance",
    "memberOf",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementConstraintType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlacementConstraintType:
    return cast(PlacementConstraintType, data)
