"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackageIngestStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.datasource_package
    import aws_sdk_detective.types.datasource_package_ingest_state

DatasourcePackageIngestStates: TypeAlias = dict[
    "aws_sdk_detective.types.datasource_package.DatasourcePackage",
    "aws_sdk_detective.types.datasource_package_ingest_state.DatasourcePackageIngestState",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DatasourcePackageIngestStates) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_detective.types.datasource_package
        import aws_sdk_detective.types.datasource_package_ingest_state

        out[aws_sdk_detective.types.datasource_package.serialize_json(key)] = (
            aws_sdk_detective.types.datasource_package_ingest_state.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> DatasourcePackageIngestStates:
    out: DatasourcePackageIngestStates = {}
    for key, value in data.items():
        import aws_sdk_detective.types.datasource_package
        import aws_sdk_detective.types.datasource_package_ingest_state

        out[aws_sdk_detective.types.datasource_package.deserialize_json(key)] = (
            aws_sdk_detective.types.datasource_package_ingest_state.deserialize_json(
                value
            )
        )
    return out
