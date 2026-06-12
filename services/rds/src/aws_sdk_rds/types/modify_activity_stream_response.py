"""Generated from Smithy shape ``com.amazonaws.rds#ModifyActivityStreamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.activity_stream_mode
    import aws_sdk_rds.types.activity_stream_policy_status
    import aws_sdk_rds.types.activity_stream_status
    import aws_sdk_rds.types.boolean_optional
    import aws_sdk_rds.types.string


class ModifyActivityStreamResponse(TypedDict):
    kms_key_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of messages in the database activity stream.</p>"""
    kinesis_stream_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the Amazon Kinesis data stream to be used for the database activity stream.</p>"""
    status: NotRequired["aws_sdk_rds.types.activity_stream_status.ActivityStreamStatus"]
    """<p>The status of the modification to the database activity stream.</p>"""
    mode: NotRequired["aws_sdk_rds.types.activity_stream_mode.ActivityStreamMode"]
    """<p>The mode of the database activity stream.</p>"""
    engine_native_audit_fields_included: NotRequired[
        "aws_sdk_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether engine-native audit fields are included in the database activity stream.</p>"""
    policy_status: NotRequired[
        "aws_sdk_rds.types.activity_stream_policy_status.ActivityStreamPolicyStatus"
    ]
    """<p>The status of the modification to the policy state of the database activity stream.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyActivityStreamResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "kinesis_stream_name" in value:
        pairs.append((f"{prefix}.KinesisStreamName", str(value["kinesis_stream_name"])))
    if "status" in value:
        import aws_sdk_rds.types.activity_stream_status

        aws_sdk_rds.types.activity_stream_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "mode" in value:
        import aws_sdk_rds.types.activity_stream_mode

        aws_sdk_rds.types.activity_stream_mode.serialize_query(
            value["mode"], pairs, f"{prefix}.Mode"
        )
    if "engine_native_audit_fields_included" in value:
        pairs.append(
            (
                f"{prefix}.EngineNativeAuditFieldsIncluded",
                "true" if value["engine_native_audit_fields_included"] else "false",
            )
        )
    if "policy_status" in value:
        import aws_sdk_rds.types.activity_stream_policy_status

        aws_sdk_rds.types.activity_stream_policy_status.serialize_query(
            value["policy_status"], pairs, f"{prefix}.PolicyStatus"
        )


def deserialize_query(el: Element) -> ModifyActivityStreamResponse:
    out: ModifyActivityStreamResponse = {}  # type: ignore[typeddict-item]
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_kinesis_stream_name = el.find("KinesisStreamName")
    if child_kinesis_stream_name is not None:
        out["kinesis_stream_name"] = str(child_kinesis_stream_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_rds.types.activity_stream_status

        out["status"] = aws_sdk_rds.types.activity_stream_status.deserialize_query(
            child_status
        )
    child_mode = el.find("Mode")
    if child_mode is not None:
        import aws_sdk_rds.types.activity_stream_mode

        out["mode"] = aws_sdk_rds.types.activity_stream_mode.deserialize_query(
            child_mode
        )
    child_engine_native_audit_fields_included = el.find(
        "EngineNativeAuditFieldsIncluded"
    )
    if child_engine_native_audit_fields_included is not None:
        out["engine_native_audit_fields_included"] = (
            child_engine_native_audit_fields_included.text or ""
        ).lower() == "true"
    child_policy_status = el.find("PolicyStatus")
    if child_policy_status is not None:
        import aws_sdk_rds.types.activity_stream_policy_status

        out["policy_status"] = (
            aws_sdk_rds.types.activity_stream_policy_status.deserialize_query(
                child_policy_status
            )
        )
    return out
