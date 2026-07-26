"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackageIngestStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.datasource_package
    import capo_detective.types.datasource_package_ingest_state

DatasourcePackageIngestStates: TypeAlias = dict[
    "capo_detective.types.datasource_package.DatasourcePackage",
    "capo_detective.types.datasource_package_ingest_state.DatasourcePackageIngestState",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DatasourcePackageIngestStates) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_detective.types.datasource_package
        import capo_detective.types.datasource_package_ingest_state

        out[capo_detective.types.datasource_package.serialize_json(key)] = (
            capo_detective.types.datasource_package_ingest_state.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> DatasourcePackageIngestStates:
    out: DatasourcePackageIngestStates = {}
    for key, value in data.items():
        import capo_detective.types.datasource_package
        import capo_detective.types.datasource_package_ingest_state

        out[capo_detective.types.datasource_package.deserialize_json(key)] = (
            capo_detective.types.datasource_package_ingest_state.deserialize_json(value)
        )
    return out
