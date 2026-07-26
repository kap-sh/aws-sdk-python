"""Generated from Smithy shape ``com.amazonaws.detective#LastIngestStateChangeDates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.datasource_package_ingest_state
    import capo_detective.types.timestamp_for_collection

LastIngestStateChangeDates: TypeAlias = dict[
    "capo_detective.types.datasource_package_ingest_state.DatasourcePackageIngestState",
    "capo_detective.types.timestamp_for_collection.TimestampForCollection",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LastIngestStateChangeDates) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_detective.types.datasource_package_ingest_state
        import capo_detective.types.timestamp_for_collection

        out[
            capo_detective.types.datasource_package_ingest_state.serialize_json(key)
        ] = capo_detective.types.timestamp_for_collection.serialize_json(value)
    return out


def deserialize_json(data: dict) -> LastIngestStateChangeDates:
    out: LastIngestStateChangeDates = {}
    for key, value in data.items():
        import capo_detective.types.datasource_package_ingest_state
        import capo_detective.types.timestamp_for_collection

        out[
            capo_detective.types.datasource_package_ingest_state.deserialize_json(key)
        ] = capo_detective.types.timestamp_for_collection.deserialize_json(value)
    return out
