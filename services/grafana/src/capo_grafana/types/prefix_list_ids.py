"""Generated from Smithy shape ``com.amazonaws.grafana#PrefixListIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_grafana.types.prefix_list_id

PrefixListIds: TypeAlias = list["capo_grafana.types.prefix_list_id.PrefixListId"]


# --- restJson1 ser/de ---
def serialize_json(value: PrefixListIds) -> list:
    return list(value)


def deserialize_json(data: list) -> PrefixListIds:
    return list(data)
