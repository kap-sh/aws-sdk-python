"""Generated from Smithy shape ``com.amazonaws.lakeformation#BatchRevokePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.batch_permissions_request_entry_list
    import aws_sdk_lakeformation.types.catalog_id_string


class BatchRevokePermissionsRequest(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    entries: "aws_sdk_lakeformation.types.batch_permissions_request_entry_list.BatchPermissionsRequestEntryList"
    """<p>A list of up to 20 entries for resource permissions to be revoked by batch operation to the principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRevokePermissionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import aws_sdk_lakeformation.types.batch_permissions_request_entry_list

    out["Entries"] = (
        aws_sdk_lakeformation.types.batch_permissions_request_entry_list.serialize_json(
            value["entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchRevokePermissionsRequest:
    out: BatchRevokePermissionsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Entries" in data:
        import aws_sdk_lakeformation.types.batch_permissions_request_entry_list

        out["entries"] = (
            aws_sdk_lakeformation.types.batch_permissions_request_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("BatchRevokePermissionsRequest.entries required")
    return out
