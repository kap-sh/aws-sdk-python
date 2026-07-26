"""Generated from Smithy shape ``com.amazonaws.quicksight#SelfUpgradeRequestDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.self_upgrade_request_detail

SelfUpgradeRequestDetailList: TypeAlias = list[
    "capo_quicksight.types.self_upgrade_request_detail.SelfUpgradeRequestDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: SelfUpgradeRequestDetailList) -> list:
    import capo_quicksight.types.self_upgrade_request_detail

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.self_upgrade_request_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SelfUpgradeRequestDetailList:
    import capo_quicksight.types.self_upgrade_request_detail

    out: SelfUpgradeRequestDetailList = []
    for item in data:
        out.append(
            capo_quicksight.types.self_upgrade_request_detail.deserialize_json(item)
        )
    return out
