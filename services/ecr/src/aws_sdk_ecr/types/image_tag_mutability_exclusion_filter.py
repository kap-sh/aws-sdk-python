"""Generated from Smithy shape ``com.amazonaws.ecr#ImageTagMutabilityExclusionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_tag_mutability_exclusion_filter_type
    import aws_sdk_ecr.types.image_tag_mutability_exclusion_filter_value


class ImageTagMutabilityExclusionFilter(TypedDict, closed=True):
    filter_type: "aws_sdk_ecr.types.image_tag_mutability_exclusion_filter_type.ImageTagMutabilityExclusionFilterType"
    """<p>The type of filter to apply for excluding image tags from mutability settings.</p>"""
    filter: "aws_sdk_ecr.types.image_tag_mutability_exclusion_filter_value.ImageTagMutabilityExclusionFilterValue"
    """<p>The filter value used to match image tags for exclusion from mutability settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagMutabilityExclusionFilter) -> dict:
    out: dict = {}
    import aws_sdk_ecr.types.image_tag_mutability_exclusion_filter_type

    out["filterType"] = (
        aws_sdk_ecr.types.image_tag_mutability_exclusion_filter_type.serialize_aws_json_1_1(
            value["filter_type"]
        )
    )
    out["filter"] = value["filter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageTagMutabilityExclusionFilter:
    out: ImageTagMutabilityExclusionFilter = {}  # type: ignore[typeddict-item]
    if "filterType" in data:
        import aws_sdk_ecr.types.image_tag_mutability_exclusion_filter_type

        out["filter_type"] = (
            aws_sdk_ecr.types.image_tag_mutability_exclusion_filter_type.deserialize_aws_json_1_1(
                data["filterType"]
            )
        )
    else:
        raise DeserializationError(
            "ImageTagMutabilityExclusionFilter.filter_type required"
        )
    if "filter" in data:
        out["filter"] = data["filter"]
    else:
        raise DeserializationError("ImageTagMutabilityExclusionFilter.filter required")
    return out
