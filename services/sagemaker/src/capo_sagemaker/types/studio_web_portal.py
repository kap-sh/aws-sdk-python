"""Generated from Smithy shape ``com.amazonaws.sagemaker#StudioWebPortal``."""

from typing import Literal, TypeAlias, cast

StudioWebPortal: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StudioWebPortal) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StudioWebPortal:
    return cast(StudioWebPortal, data)
