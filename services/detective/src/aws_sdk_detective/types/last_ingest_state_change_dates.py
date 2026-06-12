"""Generated from Smithy shape ``com.amazonaws.detective#LastIngestStateChangeDates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.datasource_package_ingest_state
    import aws_sdk_detective.types.timestamp_for_collection

LastIngestStateChangeDates: TypeAlias = dict[
    "aws_sdk_detective.types.datasource_package_ingest_state.DatasourcePackageIngestState",
    "aws_sdk_detective.types.timestamp_for_collection.TimestampForCollection",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LastIngestStateChangeDates) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_detective.types.datasource_package_ingest_state
        import aws_sdk_detective.types.timestamp_for_collection

        out[
            aws_sdk_detective.types.datasource_package_ingest_state.serialize_json(key)
        ] = aws_sdk_detective.types.timestamp_for_collection.serialize_json(value)
    return out


def deserialize_json(data: dict) -> LastIngestStateChangeDates:
    out: LastIngestStateChangeDates = {}
    for key, value in data.items():
        import aws_sdk_detective.types.datasource_package_ingest_state
        import aws_sdk_detective.types.timestamp_for_collection

        out[
            aws_sdk_detective.types.datasource_package_ingest_state.deserialize_json(
                key
            )
        ] = aws_sdk_detective.types.timestamp_for_collection.deserialize_json(value)
    return out
