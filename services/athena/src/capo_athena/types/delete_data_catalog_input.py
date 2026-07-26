"""Generated from Smithy shape ``com.amazonaws.athena#DeleteDataCatalogInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.boolean
    import capo_athena.types.catalog_name_string


class DeleteDataCatalogInput(TypedDict, closed=True):
    name: "capo_athena.types.catalog_name_string.CatalogNameString"
    """<p>The name of the data catalog to delete.</p>"""
    delete_catalog_only: "capo_athena.types.boolean.Boolean"
    """<p>Deletes the Athena Data Catalog. You can only use this with the <code>FEDERATED</code> catalogs. You usually perform this before registering the connector with Glue Data Catalog. After deletion, you will have to manage the Glue Connection and Lambda function. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataCatalogInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["DeleteCatalogOnly"] = value.get("delete_catalog_only", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataCatalogInput:
    out: DeleteDataCatalogInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteDataCatalogInput.name required")
    if "DeleteCatalogOnly" in data:
        out["delete_catalog_only"] = data["DeleteCatalogOnly"]
    else:
        out["delete_catalog_only"] = False
    return out
