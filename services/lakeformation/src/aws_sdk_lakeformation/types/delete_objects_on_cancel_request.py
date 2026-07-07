"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeleteObjectsOnCancelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.name_string
    import aws_sdk_lakeformation.types.transaction_id_string
    import aws_sdk_lakeformation.types.virtual_object_list


class DeleteObjectsOnCancelRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The Glue data catalog that contains the governed table. Defaults to the current account ID.</p>"""
    database_name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>The database that contains the governed table.</p>"""
    table_name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>The name of the governed table.</p>"""
    transaction_id: (
        "aws_sdk_lakeformation.types.transaction_id_string.TransactionIdString"
    )
    """<p>ID of the transaction that the writes occur in.</p>"""
    objects: "aws_sdk_lakeformation.types.virtual_object_list.VirtualObjectList"
    """<p>A list of VirtualObject structures, which indicates the Amazon S3 objects to be deleted if the transaction cancels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteObjectsOnCancelRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["TransactionId"] = value["transaction_id"]
    import aws_sdk_lakeformation.types.virtual_object_list

    out["Objects"] = aws_sdk_lakeformation.types.virtual_object_list.serialize_json(
        value["objects"]
    )
    return out


def deserialize_json(data: dict) -> DeleteObjectsOnCancelRequest:
    out: DeleteObjectsOnCancelRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "DeleteObjectsOnCancelRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("DeleteObjectsOnCancelRequest.table_name required")
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    else:
        raise DeserializationError(
            "DeleteObjectsOnCancelRequest.transaction_id required"
        )
    if "Objects" in data:
        import aws_sdk_lakeformation.types.virtual_object_list

        out["objects"] = (
            aws_sdk_lakeformation.types.virtual_object_list.deserialize_json(
                data["Objects"]
            )
        )
    else:
        raise DeserializationError("DeleteObjectsOnCancelRequest.objects required")
    return out
