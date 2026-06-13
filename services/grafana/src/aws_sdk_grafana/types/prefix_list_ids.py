"""Generated from Smithy shape ``com.amazonaws.grafana#PrefixListIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_grafana.types.prefix_list_id

PrefixListIds: TypeAlias = list["aws_sdk_grafana.types.prefix_list_id.PrefixListId"]


# --- restJson1 ser/de ---
def serialize_json(value: PrefixListIds) -> list:
    return list(value)


def deserialize_json(data: list) -> PrefixListIds:
    return list(data)
