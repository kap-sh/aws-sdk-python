"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EnrollmentFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.enrollment_filter

EnrollmentFilters: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.enrollment_filter.EnrollmentFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnrollmentFilters) -> list:
    import aws_sdk_compute_optimizer.types.enrollment_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.enrollment_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EnrollmentFilters:
    import aws_sdk_compute_optimizer.types.enrollment_filter

    out: EnrollmentFilters = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.enrollment_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
