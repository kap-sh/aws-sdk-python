"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingPlans``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_testing_plan_for_list

RestoreTestingPlans: TypeAlias = list[
    "aws_sdk_backup.types.restore_testing_plan_for_list.RestoreTestingPlanForList"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingPlans) -> list:
    import aws_sdk_backup.types.restore_testing_plan_for_list

    out: list = []
    for item in value:
        out.append(
            aws_sdk_backup.types.restore_testing_plan_for_list.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RestoreTestingPlans:
    import aws_sdk_backup.types.restore_testing_plan_for_list

    out: RestoreTestingPlans = []
    for item in data:
        out.append(
            aws_sdk_backup.types.restore_testing_plan_for_list.deserialize_json(item)
        )
    return out
