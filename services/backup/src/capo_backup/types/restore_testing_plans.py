"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingPlans``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.restore_testing_plan_for_list

RestoreTestingPlans: TypeAlias = list[
    "capo_backup.types.restore_testing_plan_for_list.RestoreTestingPlanForList"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingPlans) -> list:
    import capo_backup.types.restore_testing_plan_for_list

    out: list = []
    for item in value:
        out.append(capo_backup.types.restore_testing_plan_for_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> RestoreTestingPlans:
    import capo_backup.types.restore_testing_plan_for_list

    out: RestoreTestingPlans = []
    for item in data:
        out.append(
            capo_backup.types.restore_testing_plan_for_list.deserialize_json(item)
        )
    return out
