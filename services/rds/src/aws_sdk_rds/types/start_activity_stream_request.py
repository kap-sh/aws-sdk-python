"""Generated from Smithy shape ``com.amazonaws.rds#StartActivityStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.activity_stream_mode
    import aws_sdk_rds.types.boolean_optional
    import aws_sdk_rds.types.string


class StartActivityStreamRequest(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the DB cluster, for example, <code>arn:aws:rds:us-east-1:12345667890:cluster:das-cluster</code>.</p>"""
    mode: NotRequired["aws_sdk_rds.types.activity_stream_mode.ActivityStreamMode"]
    """<p>Specifies the mode of the database activity stream. Database events such as a change or access generate an activity stream event. The database session can handle these events either synchronously or asynchronously.</p>"""
    kms_key_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encrypting messages in the database activity stream. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    apply_immediately: NotRequired["aws_sdk_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether or not the database activity stream is to start as soon as possible, regardless of the maintenance window for the database.</p>"""
    engine_native_audit_fields_included: NotRequired[
        "aws_sdk_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether the database activity stream includes engine-native audit fields. This option applies to an Oracle or Microsoft SQL Server DB instance. By default, no engine-native audit fields are included.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartActivityStreamRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))
    if "mode" in value:
        import aws_sdk_rds.types.activity_stream_mode

        aws_sdk_rds.types.activity_stream_mode.serialize_query(
            value["mode"], pairs, f"{prefix}.Mode"
        )
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{prefix}.ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )
    if "engine_native_audit_fields_included" in value:
        pairs.append(
            (
                f"{prefix}.EngineNativeAuditFieldsIncluded",
                "true" if value["engine_native_audit_fields_included"] else "false",
            )
        )


def deserialize_query(el: Element) -> StartActivityStreamRequest:
    out: StartActivityStreamRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_mode = el.find("Mode")
    if child_mode is not None:
        import aws_sdk_rds.types.activity_stream_mode

        out["mode"] = aws_sdk_rds.types.activity_stream_mode.deserialize_query(
            child_mode
        )
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    child_engine_native_audit_fields_included = el.find(
        "EngineNativeAuditFieldsIncluded"
    )
    if child_engine_native_audit_fields_included is not None:
        out["engine_native_audit_fields_included"] = (
            child_engine_native_audit_fields_included.text or ""
        ).lower() == "true"
    return out
