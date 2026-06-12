"""Generated from Smithy shape ``com.amazonaws.glue#GetCatalogImportStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_import_status


class GetCatalogImportStatusResponse(TypedDict):
    import_status: NotRequired[
        "aws_sdk_glue.types.catalog_import_status.CatalogImportStatus"
    ]
    """<p>The status of the specified catalog migration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCatalogImportStatusResponse) -> dict:
    out: dict = {}
    if "import_status" in value:
        import aws_sdk_glue.types.catalog_import_status

        out["ImportStatus"] = (
            aws_sdk_glue.types.catalog_import_status.serialize_aws_json_1_1(
                value["import_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCatalogImportStatusResponse:
    out: GetCatalogImportStatusResponse = {}  # type: ignore[typeddict-item]
    if "ImportStatus" in data:
        import aws_sdk_glue.types.catalog_import_status

        out["import_status"] = (
            aws_sdk_glue.types.catalog_import_status.deserialize_aws_json_1_1(
                data["ImportStatus"]
            )
        )
    return out
