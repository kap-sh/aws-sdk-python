"""Generated from Smithy shape ``com.amazonaws.ecr#ImageTagMutabilityExclusionFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.image_tag_mutability_exclusion_filter

ImageTagMutabilityExclusionFilters: TypeAlias = list[
    "capo_ecr.types.image_tag_mutability_exclusion_filter.ImageTagMutabilityExclusionFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagMutabilityExclusionFilters) -> list:
    import capo_ecr.types.image_tag_mutability_exclusion_filter

    out: list = []
    for item in value:
        out.append(
            capo_ecr.types.image_tag_mutability_exclusion_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImageTagMutabilityExclusionFilters:
    import capo_ecr.types.image_tag_mutability_exclusion_filter

    out: ImageTagMutabilityExclusionFilters = []
    for item in data:
        out.append(
            capo_ecr.types.image_tag_mutability_exclusion_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
