"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListServerSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.server_summary

ListServerSummary: TypeAlias = list[
    "capo_migrationhubstrategy.types.server_summary.ServerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListServerSummary) -> list:
    import capo_migrationhubstrategy.types.server_summary

    out: list = []
    for item in value:
        out.append(capo_migrationhubstrategy.types.server_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListServerSummary:
    import capo_migrationhubstrategy.types.server_summary

    out: ListServerSummary = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.server_summary.deserialize_json(item)
        )
    return out
