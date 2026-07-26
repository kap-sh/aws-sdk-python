"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ServerDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.server_detail

ServerDetails: TypeAlias = list[
    "capo_migrationhubstrategy.types.server_detail.ServerDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServerDetails) -> list:
    import capo_migrationhubstrategy.types.server_detail

    out: list = []
    for item in value:
        out.append(capo_migrationhubstrategy.types.server_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServerDetails:
    import capo_migrationhubstrategy.types.server_detail

    out: ServerDetails = []
    for item in data:
        out.append(capo_migrationhubstrategy.types.server_detail.deserialize_json(item))
    return out
