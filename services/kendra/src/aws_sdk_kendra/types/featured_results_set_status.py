"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsSetStatus``."""

from typing import Literal, TypeAlias, cast

FeaturedResultsSetStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedResultsSetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeaturedResultsSetStatus:
    return cast(FeaturedResultsSetStatus, data)
