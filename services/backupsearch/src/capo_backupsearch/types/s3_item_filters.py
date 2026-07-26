"""Generated from Smithy shape ``com.amazonaws.backupsearch#S3ItemFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backupsearch.types.s3_item_filter

S3ItemFilters: TypeAlias = list["capo_backupsearch.types.s3_item_filter.S3ItemFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: S3ItemFilters) -> list:
    import capo_backupsearch.types.s3_item_filter

    out: list = []
    for item in value:
        out.append(capo_backupsearch.types.s3_item_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> S3ItemFilters:
    import capo_backupsearch.types.s3_item_filter

    out: S3ItemFilters = []
    for item in data:
        out.append(capo_backupsearch.types.s3_item_filter.deserialize_json(item))
    return out
