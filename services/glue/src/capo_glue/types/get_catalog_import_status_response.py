"""Generated from Smithy shape ``com.amazonaws.glue#GetCatalogImportStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_import_status


class GetCatalogImportStatusResponse(TypedDict, closed=True):
    import_status: NotRequired[
        "capo_glue.types.catalog_import_status.CatalogImportStatus"
    ]
    """<p>The status of the specified catalog migration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCatalogImportStatusResponse) -> dict:
    out: dict = {}
    if "import_status" in value:
        import capo_glue.types.catalog_import_status

        out["ImportStatus"] = (
            capo_glue.types.catalog_import_status.serialize_aws_json_1_1(
                value["import_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCatalogImportStatusResponse:
    out: GetCatalogImportStatusResponse = {}  # type: ignore[typeddict-item]
    if "ImportStatus" in data:
        import capo_glue.types.catalog_import_status

        out["import_status"] = (
            capo_glue.types.catalog_import_status.deserialize_aws_json_1_1(
                data["ImportStatus"]
            )
        )
    return out
