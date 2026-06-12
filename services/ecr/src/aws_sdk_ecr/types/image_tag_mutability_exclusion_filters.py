"""Generated from Smithy shape ``com.amazonaws.ecr#ImageTagMutabilityExclusionFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_tag_mutability_exclusion_filter

ImageTagMutabilityExclusionFilters: TypeAlias = list[
    "aws_sdk_ecr.types.image_tag_mutability_exclusion_filter.ImageTagMutabilityExclusionFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagMutabilityExclusionFilters) -> list:
    import aws_sdk_ecr.types.image_tag_mutability_exclusion_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr.types.image_tag_mutability_exclusion_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImageTagMutabilityExclusionFilters:
    import aws_sdk_ecr.types.image_tag_mutability_exclusion_filter

    out: ImageTagMutabilityExclusionFilters = []
    for item in data:
        out.append(
            aws_sdk_ecr.types.image_tag_mutability_exclusion_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
