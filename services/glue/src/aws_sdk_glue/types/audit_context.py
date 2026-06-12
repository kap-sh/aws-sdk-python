"""Generated from Smithy shape ``com.amazonaws.glue#AuditContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.audit_column_names_list
    import aws_sdk_glue.types.audit_context_string
    import aws_sdk_glue.types.nullable_boolean


class AuditContext(TypedDict):
    additional_audit_context: NotRequired[
        "aws_sdk_glue.types.audit_context_string.AuditContextString"
    ]
    """<p>A string containing the additional audit context information.</p>"""
    requested_columns: NotRequired[
        "aws_sdk_glue.types.audit_column_names_list.AuditColumnNamesList"
    ]
    """<p>The requested columns for audit.</p>"""
    all_columns_requested: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>All columns request for audit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuditContext) -> dict:
    out: dict = {}
    if "additional_audit_context" in value:
        out["AdditionalAuditContext"] = value["additional_audit_context"]
    if "requested_columns" in value:
        import aws_sdk_glue.types.audit_column_names_list

        out["RequestedColumns"] = (
            aws_sdk_glue.types.audit_column_names_list.serialize_aws_json_1_1(
                value["requested_columns"]
            )
        )
    if "all_columns_requested" in value:
        out["AllColumnsRequested"] = value["all_columns_requested"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AuditContext:
    out: AuditContext = {}  # type: ignore[typeddict-item]
    if "AdditionalAuditContext" in data:
        out["additional_audit_context"] = data["AdditionalAuditContext"]
    if "RequestedColumns" in data:
        import aws_sdk_glue.types.audit_column_names_list

        out["requested_columns"] = (
            aws_sdk_glue.types.audit_column_names_list.deserialize_aws_json_1_1(
                data["RequestedColumns"]
            )
        )
    if "AllColumnsRequested" in data:
        out["all_columns_requested"] = data["AllColumnsRequested"]
    return out
