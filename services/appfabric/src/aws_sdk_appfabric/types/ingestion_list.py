"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.ingestion_summary

IngestionList: TypeAlias = list[
    "aws_sdk_appfabric.types.ingestion_summary.IngestionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionList) -> list:
    import aws_sdk_appfabric.types.ingestion_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_appfabric.types.ingestion_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> IngestionList:
    import aws_sdk_appfabric.types.ingestion_summary

    out: IngestionList = []
    for item in data:
        out.append(aws_sdk_appfabric.types.ingestion_summary.deserialize_json(item))
    return out
