"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AccountEnrollmentStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_enrollment_status

AccountEnrollmentStatuses: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.account_enrollment_status.AccountEnrollmentStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountEnrollmentStatuses) -> list:
    import aws_sdk_compute_optimizer.types.account_enrollment_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.account_enrollment_status.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AccountEnrollmentStatuses:
    import aws_sdk_compute_optimizer.types.account_enrollment_status

    out: AccountEnrollmentStatuses = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.account_enrollment_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out
