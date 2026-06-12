"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.ingestion_destination_summary

IngestionDestinationList: TypeAlias = list[
    "aws_sdk_appfabric.types.ingestion_destination_summary.IngestionDestinationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionDestinationList) -> list:
    import aws_sdk_appfabric.types.ingestion_destination_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appfabric.types.ingestion_destination_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IngestionDestinationList:
    import aws_sdk_appfabric.types.ingestion_destination_summary

    out: IngestionDestinationList = []
    for item in data:
        out.append(
            aws_sdk_appfabric.types.ingestion_destination_summary.deserialize_json(item)
        )
    return out
