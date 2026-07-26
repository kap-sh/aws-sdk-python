"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_summary

TableBucketSummaryList: TypeAlias = list[
    "capo_s3tables.types.table_bucket_summary.TableBucketSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketSummaryList) -> list:
    import capo_s3tables.types.table_bucket_summary

    out: list = []
    for item in value:
        out.append(capo_s3tables.types.table_bucket_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TableBucketSummaryList:
    import capo_s3tables.types.table_bucket_summary

    out: TableBucketSummaryList = []
    for item in data:
        out.append(capo_s3tables.types.table_bucket_summary.deserialize_json(item))
    return out
