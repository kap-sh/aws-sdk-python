"""Generated from Smithy shape ``com.amazonaws.rds#StartActivityStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.activity_stream_mode
    import capo_rds.types.activity_stream_status
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.string


class StartActivityStreamResponse(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of messages in the database activity stream.</p>"""
    kinesis_stream_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the Amazon Kinesis data stream to be used for the database activity stream.</p>"""
    status: NotRequired["capo_rds.types.activity_stream_status.ActivityStreamStatus"]
    """<p>The status of the database activity stream.</p>"""
    mode: NotRequired["capo_rds.types.activity_stream_mode.ActivityStreamMode"]
    """<p>The mode of the database activity stream.</p>"""
    engine_native_audit_fields_included: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether engine-native audit fields are included in the database activity stream.</p>"""
    apply_immediately: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether or not the database activity stream will start as soon as possible, regardless of the maintenance window for the database.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartActivityStreamResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "kinesis_stream_name" in value:
        pairs.append((f"{prefix}.KinesisStreamName", str(value["kinesis_stream_name"])))
    if "status" in value:
        import capo_rds.types.activity_stream_status

        capo_rds.types.activity_stream_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "mode" in value:
        import capo_rds.types.activity_stream_mode

        capo_rds.types.activity_stream_mode.serialize_query(
            value["mode"], pairs, f"{prefix}.Mode"
        )
    if "engine_native_audit_fields_included" in value:
        pairs.append(
            (
                f"{prefix}.EngineNativeAuditFieldsIncluded",
                "true" if value["engine_native_audit_fields_included"] else "false",
            )
        )
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{prefix}.ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )


def deserialize_query(el: Element) -> StartActivityStreamResponse:
    out: StartActivityStreamResponse = {}  # type: ignore[typeddict-item]
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_kinesis_stream_name = el.find("KinesisStreamName")
    if child_kinesis_stream_name is not None:
        out["kinesis_stream_name"] = str(child_kinesis_stream_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_rds.types.activity_stream_status

        out["status"] = capo_rds.types.activity_stream_status.deserialize_query(
            child_status
        )
    child_mode = el.find("Mode")
    if child_mode is not None:
        import capo_rds.types.activity_stream_mode

        out["mode"] = capo_rds.types.activity_stream_mode.deserialize_query(child_mode)
    child_engine_native_audit_fields_included = el.find(
        "EngineNativeAuditFieldsIncluded"
    )
    if child_engine_native_audit_fields_included is not None:
        out["engine_native_audit_fields_included"] = (
            child_engine_native_audit_fields_included.text or ""
        ).lower() == "true"
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    return out
