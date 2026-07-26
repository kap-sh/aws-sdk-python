"""Generated from Smithy shape ``com.amazonaws.athena#DeleteDataCatalogOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.data_catalog


class DeleteDataCatalogOutput(TypedDict, closed=True):
    data_catalog: NotRequired["capo_athena.types.data_catalog.DataCatalog"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataCatalogOutput) -> dict:
    out: dict = {}
    if "data_catalog" in value:
        import capo_athena.types.data_catalog

        out["DataCatalog"] = capo_athena.types.data_catalog.serialize_aws_json_1_1(
            value["data_catalog"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataCatalogOutput:
    out: DeleteDataCatalogOutput = {}  # type: ignore[typeddict-item]
    if "DataCatalog" in data:
        import capo_athena.types.data_catalog

        out["data_catalog"] = capo_athena.types.data_catalog.deserialize_aws_json_1_1(
            data["DataCatalog"]
        )
    return out
