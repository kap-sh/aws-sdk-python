"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateTableObjectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.name_string
    import aws_sdk_lakeformation.types.transaction_id_string
    import aws_sdk_lakeformation.types.write_operation_list


class UpdateTableObjectsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The catalog containing the governed table to update. Defaults to the caller’s account ID.</p>"""
    database_name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>The database containing the governed table to update.</p>"""
    table_name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>The governed table to update.</p>"""
    transaction_id: NotRequired[
        "aws_sdk_lakeformation.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction at which to do the write.</p>"""
    write_operations: (
        "aws_sdk_lakeformation.types.write_operation_list.WriteOperationList"
    )
    """<p>A list of <code>WriteOperation</code> objects that define an object to add to or delete from the manifest for a governed table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableObjectsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    import aws_sdk_lakeformation.types.write_operation_list

    out["WriteOperations"] = (
        aws_sdk_lakeformation.types.write_operation_list.serialize_json(
            value["write_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTableObjectsRequest:
    out: UpdateTableObjectsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("UpdateTableObjectsRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("UpdateTableObjectsRequest.table_name required")
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    if "WriteOperations" in data:
        import aws_sdk_lakeformation.types.write_operation_list

        out["write_operations"] = (
            aws_sdk_lakeformation.types.write_operation_list.deserialize_json(
                data["WriteOperations"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTableObjectsRequest.write_operations required"
        )
    return out
