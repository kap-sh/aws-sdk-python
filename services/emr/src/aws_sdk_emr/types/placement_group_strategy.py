"""Generated from Smithy shape ``com.amazonaws.emr#PlacementGroupStrategy``."""

from typing import Literal, TypeAlias, cast

PlacementGroupStrategy: TypeAlias = Literal[
    "SPREAD",
    "PARTITION",
    "CLUSTER",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementGroupStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlacementGroupStrategy:
    return cast(PlacementGroupStrategy, data)
