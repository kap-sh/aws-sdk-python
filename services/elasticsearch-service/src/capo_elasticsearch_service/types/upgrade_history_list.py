"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpgradeHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.upgrade_history

UpgradeHistoryList: TypeAlias = list[
    "capo_elasticsearch_service.types.upgrade_history.UpgradeHistory"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeHistoryList) -> list:
    import capo_elasticsearch_service.types.upgrade_history

    out: list = []
    for item in value:
        out.append(
            capo_elasticsearch_service.types.upgrade_history.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UpgradeHistoryList:
    import capo_elasticsearch_service.types.upgrade_history

    out: UpgradeHistoryList = []
    for item in data:
        out.append(
            capo_elasticsearch_service.types.upgrade_history.deserialize_json(item)
        )
    return out
