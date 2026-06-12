"""Generated from Smithy shape ``com.amazonaws.athena#CreateDataCatalogOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.data_catalog


class CreateDataCatalogOutput(TypedDict):
    data_catalog: NotRequired["aws_sdk_athena.types.data_catalog.DataCatalog"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataCatalogOutput) -> dict:
    out: dict = {}
    if "data_catalog" in value:
        import aws_sdk_athena.types.data_catalog

        out["DataCatalog"] = aws_sdk_athena.types.data_catalog.serialize_aws_json_1_1(
            value["data_catalog"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataCatalogOutput:
    out: CreateDataCatalogOutput = {}  # type: ignore[typeddict-item]
    if "DataCatalog" in data:
        import aws_sdk_athena.types.data_catalog

        out["data_catalog"] = (
            aws_sdk_athena.types.data_catalog.deserialize_aws_json_1_1(
                data["DataCatalog"]
            )
        )
    return out
