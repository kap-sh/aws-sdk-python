"""Generated from Smithy shape ``com.amazonaws.shield#SubResourceType``."""

from typing import Literal, TypeAlias, cast

SubResourceType: TypeAlias = Literal[
    "IP",
    "URL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubResourceType:
    return cast(SubResourceType, data)
