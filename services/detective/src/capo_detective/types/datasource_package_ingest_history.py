"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackageIngestHistory``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.datasource_package
    import capo_detective.types.last_ingest_state_change_dates

DatasourcePackageIngestHistory: TypeAlias = dict[
    "capo_detective.types.datasource_package.DatasourcePackage",
    "capo_detective.types.last_ingest_state_change_dates.LastIngestStateChangeDates",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DatasourcePackageIngestHistory) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_detective.types.datasource_package
        import capo_detective.types.last_ingest_state_change_dates

        out[capo_detective.types.datasource_package.serialize_json(key)] = (
            capo_detective.types.last_ingest_state_change_dates.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> DatasourcePackageIngestHistory:
    out: DatasourcePackageIngestHistory = {}
    for key, value in data.items():
        import capo_detective.types.datasource_package
        import capo_detective.types.last_ingest_state_change_dates

        out[capo_detective.types.datasource_package.deserialize_json(key)] = (
            capo_detective.types.last_ingest_state_change_dates.deserialize_json(value)
        )
    return out
