"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListServerStatusSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.server_status_summary

ListServerStatusSummary: TypeAlias = list[
    "capo_migrationhubstrategy.types.server_status_summary.ServerStatusSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListServerStatusSummary) -> list:
    import capo_migrationhubstrategy.types.server_status_summary

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.server_status_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListServerStatusSummary:
    import capo_migrationhubstrategy.types.server_status_summary

    out: ListServerStatusSummary = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.server_status_summary.deserialize_json(item)
        )
    return out
