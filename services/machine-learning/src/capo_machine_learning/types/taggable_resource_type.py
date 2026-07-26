"""Generated from Smithy shape ``com.amazonaws.machinelearning#TaggableResourceType``."""

from typing import Literal, TypeAlias, cast

TaggableResourceType: TypeAlias = Literal[
    "BatchPrediction",
    "DataSource",
    "Evaluation",
    "MLModel",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaggableResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaggableResourceType:
    return cast(TaggableResourceType, data)
