"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.update_replication_set_action

UpdateActionList: TypeAlias = list[
    "capo_ssm_incidents.types.update_replication_set_action.UpdateReplicationSetAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActionList) -> list:
    import capo_ssm_incidents.types.update_replication_set_action

    out: list = []
    for item in value:
        out.append(
            capo_ssm_incidents.types.update_replication_set_action.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UpdateActionList:
    import capo_ssm_incidents.types.update_replication_set_action

    out: UpdateActionList = []
    for item in data:
        out.append(
            capo_ssm_incidents.types.update_replication_set_action.deserialize_json(
                item
            )
        )
    return out
