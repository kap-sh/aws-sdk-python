"""Generated from Smithy shape ``com.amazonaws.redshift#Integration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.description
    import aws_sdk_redshift.types.encryption_context_map
    import aws_sdk_redshift.types.integration_arn
    import aws_sdk_redshift.types.integration_error_list
    import aws_sdk_redshift.types.integration_name
    import aws_sdk_redshift.types.source_arn
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp
    import aws_sdk_redshift.types.tag_list
    import aws_sdk_redshift.types.target_arn
    import aws_sdk_redshift.types.zero_etl_integration_status


class Integration(TypedDict, closed=True):
    integration_arn: NotRequired[
        "aws_sdk_redshift.types.integration_arn.IntegrationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the integration.</p>"""
    integration_name: NotRequired[
        "aws_sdk_redshift.types.integration_name.IntegrationName"
    ]
    """<p>The name of the integration.</p>"""
    source_arn: NotRequired["aws_sdk_redshift.types.source_arn.SourceArn"]
    """<p>The Amazon Resource Name (ARN) of the database used as the source for replication.</p>"""
    target_arn: NotRequired["aws_sdk_redshift.types.target_arn.TargetArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Redshift data warehouse to use as the target for replication.</p>"""
    status: NotRequired[
        "aws_sdk_redshift.types.zero_etl_integration_status.ZeroETLIntegrationStatus"
    ]
    """<p>The current status of the integration.</p>"""
    errors: NotRequired[
        "aws_sdk_redshift.types.integration_error_list.IntegrationErrorList"
    ]
    """<p>Any errors associated with the integration.</p>"""
    create_time: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The time (UTC) when the integration was created.</p>"""
    description: NotRequired["aws_sdk_redshift.types.description.Description"]
    """<p>The description of the integration.</p>"""
    kms_key_id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Key Management Service (KMS) key identifier for the key used to encrypt the integration.</p>"""
    additional_encryption_context: NotRequired[
        "aws_sdk_redshift.types.encryption_context_map.EncryptionContextMap"
    ]
    r"""<p>The encryption context for the integration. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context\">Encryption context</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_redshift.types.tag_list.TagList"]
    """<p>The list of tags associated with the integration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Integration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "integration_arn" in value:
        pairs.append((f"{prefix}.IntegrationArn", str(value["integration_arn"])))
    if "integration_name" in value:
        pairs.append((f"{prefix}.IntegrationName", str(value["integration_name"])))
    if "source_arn" in value:
        pairs.append((f"{prefix}.SourceArn", str(value["source_arn"])))
    if "target_arn" in value:
        pairs.append((f"{prefix}.TargetArn", str(value["target_arn"])))
    if "status" in value:
        import aws_sdk_redshift.types.zero_etl_integration_status

        aws_sdk_redshift.types.zero_etl_integration_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "errors" in value:
        import aws_sdk_redshift.types.integration_error_list

        aws_sdk_redshift.types.integration_error_list.serialize_query(
            value["errors"], pairs, f"{prefix}.Errors"
        )
    if "create_time" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["create_time"], pairs, f"{prefix}.CreateTime"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KMSKeyId", str(value["kms_key_id"])))
    if "additional_encryption_context" in value:
        import aws_sdk_redshift.types.encryption_context_map

        aws_sdk_redshift.types.encryption_context_map.serialize_query(
            value["additional_encryption_context"],
            pairs,
            f"{prefix}.AdditionalEncryptionContext",
        )
    if "tags" in value:
        import aws_sdk_redshift.types.tag_list

        aws_sdk_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> Integration:
    out: Integration = {}  # type: ignore[typeddict-item]
    child_integration_arn = el.find("IntegrationArn")
    if child_integration_arn is not None:
        out["integration_arn"] = str(child_integration_arn.text or "")
    child_integration_name = el.find("IntegrationName")
    if child_integration_name is not None:
        out["integration_name"] = str(child_integration_name.text or "")
    child_source_arn = el.find("SourceArn")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    child_target_arn = el.find("TargetArn")
    if child_target_arn is not None:
        out["target_arn"] = str(child_target_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_redshift.types.zero_etl_integration_status

        out["status"] = (
            aws_sdk_redshift.types.zero_etl_integration_status.deserialize_query(
                child_status
            )
        )
    child_errors = el.find("Errors")
    if child_errors is not None:
        import aws_sdk_redshift.types.integration_error_list

        out["errors"] = aws_sdk_redshift.types.integration_error_list.deserialize_query(
            child_errors
        )
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import aws_sdk_redshift.types.t_stamp

        out["create_time"] = aws_sdk_redshift.types.t_stamp.deserialize_query(
            child_create_time
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_kms_key_id = el.find("KMSKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_additional_encryption_context = el.find("AdditionalEncryptionContext")
    if child_additional_encryption_context is not None:
        import aws_sdk_redshift.types.encryption_context_map

        out["additional_encryption_context"] = (
            aws_sdk_redshift.types.encryption_context_map.deserialize_query(
                child_additional_encryption_context
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_redshift.types.tag_list

        out["tags"] = aws_sdk_redshift.types.tag_list.deserialize_query(child_tags)
    return out
