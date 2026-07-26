"""Generated from Smithy shape ``com.amazonaws.ecr#ImageTagMutabilityExclusionFilterType``."""

from typing import Literal, TypeAlias, cast

ImageTagMutabilityExclusionFilterType: TypeAlias = Literal["WILDCARD",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagMutabilityExclusionFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageTagMutabilityExclusionFilterType:
    return cast(ImageTagMutabilityExclusionFilterType, data)
