"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrackingServerSize``."""

from typing import Literal, TypeAlias, cast

TrackingServerSize: TypeAlias = Literal[
    "Small",
    "Medium",
    "Large",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrackingServerSize) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrackingServerSize:
    return cast(TrackingServerSize, data)
