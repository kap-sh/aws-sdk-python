"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#AccountEnrollmentStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.account_enrollment_status

AccountEnrollmentStatuses: TypeAlias = list[
    "capo_cost_optimization_hub.types.account_enrollment_status.AccountEnrollmentStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountEnrollmentStatuses) -> list:
    import capo_cost_optimization_hub.types.account_enrollment_status

    out: list = []
    for item in value:
        out.append(
            capo_cost_optimization_hub.types.account_enrollment_status.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AccountEnrollmentStatuses:
    import capo_cost_optimization_hub.types.account_enrollment_status

    out: AccountEnrollmentStatuses = []
    for item in data:
        out.append(
            capo_cost_optimization_hub.types.account_enrollment_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out
