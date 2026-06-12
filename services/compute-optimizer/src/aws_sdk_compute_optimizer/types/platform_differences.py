"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PlatformDifferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.platform_difference

PlatformDifferences: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.platform_difference.PlatformDifference"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PlatformDifferences) -> list:
    import aws_sdk_compute_optimizer.types.platform_difference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.platform_difference.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PlatformDifferences:
    import aws_sdk_compute_optimizer.types.platform_difference

    out: PlatformDifferences = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.platform_difference.deserialize_aws_json_1_0(
                item
            )
        )
    return out
