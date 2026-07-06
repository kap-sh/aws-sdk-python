"""Generated from Smithy shape ``com.amazonaws.glue#DeleteTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.transaction_id_string


class DeleteTableRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>"""
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the table to be deleted. For Hive compatibility, this name is entirely lowercase.</p>"""
    transaction_id: NotRequired[
        "aws_sdk_glue.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction ID at which to delete the table contents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTableRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["Name"] = value["name"]
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTableRequest:
    out: DeleteTableRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("DeleteTableRequest.database_name required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteTableRequest.name required")
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    return out
