"""Generated from Smithy shape ``com.amazonaws.opensearch#UpgradeStepsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.upgrade_step_item

UpgradeStepsList: TypeAlias = list[
    "capo_opensearch.types.upgrade_step_item.UpgradeStepItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeStepsList) -> list:
    import capo_opensearch.types.upgrade_step_item

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.upgrade_step_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpgradeStepsList:
    import capo_opensearch.types.upgrade_step_item

    out: UpgradeStepsList = []
    for item in data:
        out.append(capo_opensearch.types.upgrade_step_item.deserialize_json(item))
    return out
