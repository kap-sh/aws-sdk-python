"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackageIngestDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.datasource_package
    import capo_detective.types.datasource_package_ingest_detail

DatasourcePackageIngestDetails: TypeAlias = dict[
    "capo_detective.types.datasource_package.DatasourcePackage",
    "capo_detective.types.datasource_package_ingest_detail.DatasourcePackageIngestDetail",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DatasourcePackageIngestDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_detective.types.datasource_package
        import capo_detective.types.datasource_package_ingest_detail

        out[capo_detective.types.datasource_package.serialize_json(key)] = (
            capo_detective.types.datasource_package_ingest_detail.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> DatasourcePackageIngestDetails:
    out: DatasourcePackageIngestDetails = {}
    for key, value in data.items():
        import capo_detective.types.datasource_package
        import capo_detective.types.datasource_package_ingest_detail

        out[capo_detective.types.datasource_package.deserialize_json(key)] = (
            capo_detective.types.datasource_package_ingest_detail.deserialize_json(
                value
            )
        )
    return out
