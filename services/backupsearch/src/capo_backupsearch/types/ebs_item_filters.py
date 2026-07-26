"""Generated from Smithy shape ``com.amazonaws.backupsearch#EBSItemFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backupsearch.types.ebs_item_filter

EBSItemFilters: TypeAlias = list[
    "capo_backupsearch.types.ebs_item_filter.EBSItemFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: EBSItemFilters) -> list:
    import capo_backupsearch.types.ebs_item_filter

    out: list = []
    for item in value:
        out.append(capo_backupsearch.types.ebs_item_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> EBSItemFilters:
    import capo_backupsearch.types.ebs_item_filter

    out: EBSItemFilters = []
    for item in data:
        out.append(capo_backupsearch.types.ebs_item_filter.deserialize_json(item))
    return out
