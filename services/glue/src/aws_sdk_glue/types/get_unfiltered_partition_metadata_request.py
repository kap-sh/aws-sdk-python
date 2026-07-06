"""Generated from Smithy shape ``com.amazonaws.glue#GetUnfilteredPartitionMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.audit_context
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.permission_type_list
    import aws_sdk_glue.types.query_session_context
    import aws_sdk_glue.types.value_string
    import aws_sdk_glue.types.value_string_list


class GetUnfilteredPartitionMetadataRequest(TypedDict, closed=True):
    region: NotRequired["aws_sdk_glue.types.value_string.ValueString"]
    """<p>Specified only if the base tables belong to a different Amazon Web Services Region.</p>"""
    catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
    """<p>The catalog ID where the partition resides.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>(Required) Specifies the name of a database that contains the partition.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>(Required) Specifies the name of a table that contains the partition.</p>"""
    partition_values: "aws_sdk_glue.types.value_string_list.ValueStringList"
    """<p>(Required) A list of partition key values.</p>"""
    audit_context: NotRequired["aws_sdk_glue.types.audit_context.AuditContext"]
    """<p>A structure containing Lake Formation audit context information.</p>"""
    supported_permission_types: (
        "aws_sdk_glue.types.permission_type_list.PermissionTypeList"
    )
    """<p>(Required) A list of supported permission types. </p>"""
    query_session_context: NotRequired[
        "aws_sdk_glue.types.query_session_context.QuerySessionContext"
    ]
    """<p>A structure used as a protocol between query engines and Lake Formation or Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUnfilteredPartitionMetadataRequest) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_glue.types.value_string_list

    out["PartitionValues"] = (
        aws_sdk_glue.types.value_string_list.serialize_aws_json_1_1(
            value["partition_values"]
        )
    )
    if "audit_context" in value:
        import aws_sdk_glue.types.audit_context

        out["AuditContext"] = aws_sdk_glue.types.audit_context.serialize_aws_json_1_1(
            value["audit_context"]
        )
    import aws_sdk_glue.types.permission_type_list

    out["SupportedPermissionTypes"] = (
        aws_sdk_glue.types.permission_type_list.serialize_aws_json_1_1(
            value["supported_permission_types"]
        )
    )
    if "query_session_context" in value:
        import aws_sdk_glue.types.query_session_context

        out["QuerySessionContext"] = (
            aws_sdk_glue.types.query_session_context.serialize_aws_json_1_1(
                value["query_session_context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUnfilteredPartitionMetadataRequest:
    out: GetUnfilteredPartitionMetadataRequest = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError(
            "GetUnfilteredPartitionMetadataRequest.catalog_id required"
        )
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "GetUnfilteredPartitionMetadataRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "GetUnfilteredPartitionMetadataRequest.table_name required"
        )
    if "PartitionValues" in data:
        import aws_sdk_glue.types.value_string_list

        out["partition_values"] = (
            aws_sdk_glue.types.value_string_list.deserialize_aws_json_1_1(
                data["PartitionValues"]
            )
        )
    else:
        raise DeserializationError(
            "GetUnfilteredPartitionMetadataRequest.partition_values required"
        )
    if "AuditContext" in data:
        import aws_sdk_glue.types.audit_context

        out["audit_context"] = (
            aws_sdk_glue.types.audit_context.deserialize_aws_json_1_1(
                data["AuditContext"]
            )
        )
    if "SupportedPermissionTypes" in data:
        import aws_sdk_glue.types.permission_type_list

        out["supported_permission_types"] = (
            aws_sdk_glue.types.permission_type_list.deserialize_aws_json_1_1(
                data["SupportedPermissionTypes"]
            )
        )
    else:
        raise DeserializationError(
            "GetUnfilteredPartitionMetadataRequest.supported_permission_types required"
        )
    if "QuerySessionContext" in data:
        import aws_sdk_glue.types.query_session_context

        out["query_session_context"] = (
            aws_sdk_glue.types.query_session_context.deserialize_aws_json_1_1(
                data["QuerySessionContext"]
            )
        )
    return out
