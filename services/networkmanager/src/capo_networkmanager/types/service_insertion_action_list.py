"""Generated from Smithy shape ``com.amazonaws.networkmanager#ServiceInsertionActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.service_insertion_action

ServiceInsertionActionList: TypeAlias = list[
    "capo_networkmanager.types.service_insertion_action.ServiceInsertionAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceInsertionActionList) -> list:
    import capo_networkmanager.types.service_insertion_action

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.service_insertion_action.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceInsertionActionList:
    import capo_networkmanager.types.service_insertion_action

    out: ServiceInsertionActionList = []
    for item in data:
        out.append(
            capo_networkmanager.types.service_insertion_action.deserialize_json(item)
        )
    return out
