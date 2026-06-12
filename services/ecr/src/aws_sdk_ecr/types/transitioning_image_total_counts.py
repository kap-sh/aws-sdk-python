"""Generated from Smithy shape ``com.amazonaws.ecr#TransitioningImageTotalCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.transitioning_image_total_count

TransitioningImageTotalCounts: TypeAlias = list[
    "aws_sdk_ecr.types.transitioning_image_total_count.TransitioningImageTotalCount"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransitioningImageTotalCounts) -> list:
    import aws_sdk_ecr.types.transitioning_image_total_count

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr.types.transitioning_image_total_count.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TransitioningImageTotalCounts:
    import aws_sdk_ecr.types.transitioning_image_total_count

    out: TransitioningImageTotalCounts = []
    for item in data:
        out.append(
            aws_sdk_ecr.types.transitioning_image_total_count.deserialize_aws_json_1_1(
                item
            )
        )
    return out
