"""Generated from Smithy shape ``com.amazonaws.glue#GetPartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.audit_context
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.value_string_list


class GetPartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partition in question resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the partition resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the partition's table.</p>"""
    partition_values: "capo_glue.types.value_string_list.ValueStringList"
    """<p>The values that define the partition.</p>"""
    audit_context: NotRequired["capo_glue.types.audit_context.AuditContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.value_string_list

    out["PartitionValues"] = capo_glue.types.value_string_list.serialize_aws_json_1_1(
        value["partition_values"]
    )
    if "audit_context" in value:
        import capo_glue.types.audit_context

        out["AuditContext"] = capo_glue.types.audit_context.serialize_aws_json_1_1(
            value["audit_context"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPartitionRequest:
    out: GetPartitionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetPartitionRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("GetPartitionRequest.table_name required")
    if "PartitionValues" in data:
        import capo_glue.types.value_string_list

        out["partition_values"] = (
            capo_glue.types.value_string_list.deserialize_aws_json_1_1(
                data["PartitionValues"]
            )
        )
    else:
        raise DeserializationError("GetPartitionRequest.partition_values required")
    if "AuditContext" in data:
        import capo_glue.types.audit_context

        out["audit_context"] = capo_glue.types.audit_context.deserialize_aws_json_1_1(
            data["AuditContext"]
        )
    return out
