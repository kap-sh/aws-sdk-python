"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortAssociationsBy``."""

from typing import Literal, TypeAlias, cast

SortAssociationsBy: TypeAlias = Literal[
    "SourceArn",
    "DestinationArn",
    "SourceType",
    "DestinationType",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortAssociationsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortAssociationsBy:
    return cast(SortAssociationsBy, data)
