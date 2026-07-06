"""Generated from Smithy shape ``com.amazonaws.glue#ModifyIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_additional_encryption_context_map
    import aws_sdk_glue.types.integration_config
    import aws_sdk_glue.types.integration_description
    import aws_sdk_glue.types.integration_error_list
    import aws_sdk_glue.types.integration_status
    import aws_sdk_glue.types.integration_tags_list
    import aws_sdk_glue.types.integration_timestamp
    import aws_sdk_glue.types.string128
    import aws_sdk_glue.types.string512
    import aws_sdk_glue.types.string2048


class ModifyIntegrationResponse(TypedDict, closed=True):
    source_arn: "aws_sdk_glue.types.string512.String512"
    """<p>The ARN of the source for the integration.</p>"""
    target_arn: "aws_sdk_glue.types.string512.String512"
    """<p>The ARN of the target for the integration.</p>"""
    integration_name: "aws_sdk_glue.types.string128.String128"
    """<p>A unique name for an integration in Glue.</p>"""
    description: NotRequired[
        "aws_sdk_glue.types.integration_description.IntegrationDescription"
    ]
    """<p>A description of the integration.</p>"""
    integration_arn: "aws_sdk_glue.types.string128.String128"
    """<p>The Amazon Resource Name (ARN) for the integration.</p>"""
    kms_key_id: NotRequired["aws_sdk_glue.types.string2048.String2048"]
    """<p>The ARN of a KMS key used for encrypting the channel.</p>"""
    additional_encryption_context: NotRequired[
        "aws_sdk_glue.types.integration_additional_encryption_context_map.IntegrationAdditionalEncryptionContextMap"
    ]
    """<p>An optional set of non-secret key–value pairs that contains additional contextual information for encryption.</p>"""
    tags: NotRequired["aws_sdk_glue.types.integration_tags_list.IntegrationTagsList"]
    """<p>Metadata assigned to the resource consisting of a list of key-value pairs.</p>"""
    status: "aws_sdk_glue.types.integration_status.IntegrationStatus"
    """<p>The status of the integration being modified.</p> <p>The possible statuses are:</p> <ul> <li> <p>CREATING: The integration is being created.</p> </li> <li> <p>ACTIVE: The integration creation succeeds.</p> </li> <li> <p>MODIFYING: The integration is being modified.</p> </li> <li> <p>FAILED: The integration creation fails. </p> </li> <li> <p>DELETING: The integration is deleted.</p> </li> <li> <p>SYNCING: The integration is synchronizing.</p> </li> <li> <p>NEEDS_ATTENTION: The integration needs attention, such as synchronization.</p> </li> </ul>"""
    create_time: "aws_sdk_glue.types.integration_timestamp.IntegrationTimestamp"
    """<p>The time when the integration was created, in UTC.</p>"""
    errors: NotRequired[
        "aws_sdk_glue.types.integration_error_list.IntegrationErrorList"
    ]
    """<p>A list of errors associated with the integration modification.</p>"""
    data_filter: NotRequired["aws_sdk_glue.types.string2048.String2048"]
    """<p>Selects source tables for the integration using Maxwell filter syntax.</p>"""
    integration_config: NotRequired[
        "aws_sdk_glue.types.integration_config.IntegrationConfig"
    ]
    """<p>The updated configuration settings for the integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyIntegrationResponse) -> dict:
    out: dict = {}
    out["SourceArn"] = value["source_arn"]
    out["TargetArn"] = value["target_arn"]
    out["IntegrationName"] = value["integration_name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["IntegrationArn"] = value["integration_arn"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "additional_encryption_context" in value:
        import aws_sdk_glue.types.integration_additional_encryption_context_map

        out["AdditionalEncryptionContext"] = (
            aws_sdk_glue.types.integration_additional_encryption_context_map.serialize_aws_json_1_1(
                value["additional_encryption_context"]
            )
        )
    if "tags" in value:
        import aws_sdk_glue.types.integration_tags_list

        out["Tags"] = aws_sdk_glue.types.integration_tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    import aws_sdk_glue.types.integration_status

    out["Status"] = aws_sdk_glue.types.integration_status.serialize_aws_json_1_1(
        value["status"]
    )
    import aws_sdk_glue.types.integration_timestamp

    out["CreateTime"] = aws_sdk_glue.types.integration_timestamp.serialize_aws_json_1_1(
        value["create_time"]
    )
    if "errors" in value:
        import aws_sdk_glue.types.integration_error_list

        out["Errors"] = (
            aws_sdk_glue.types.integration_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    if "data_filter" in value:
        out["DataFilter"] = value["data_filter"]
    if "integration_config" in value:
        import aws_sdk_glue.types.integration_config

        out["IntegrationConfig"] = (
            aws_sdk_glue.types.integration_config.serialize_aws_json_1_1(
                value["integration_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyIntegrationResponse:
    out: ModifyIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    else:
        raise DeserializationError("ModifyIntegrationResponse.source_arn required")
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    else:
        raise DeserializationError("ModifyIntegrationResponse.target_arn required")
    if "IntegrationName" in data:
        out["integration_name"] = data["IntegrationName"]
    else:
        raise DeserializationError(
            "ModifyIntegrationResponse.integration_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "IntegrationArn" in data:
        out["integration_arn"] = data["IntegrationArn"]
    else:
        raise DeserializationError("ModifyIntegrationResponse.integration_arn required")
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "AdditionalEncryptionContext" in data:
        import aws_sdk_glue.types.integration_additional_encryption_context_map

        out["additional_encryption_context"] = (
            aws_sdk_glue.types.integration_additional_encryption_context_map.deserialize_aws_json_1_1(
                data["AdditionalEncryptionContext"]
            )
        )
    if "Tags" in data:
        import aws_sdk_glue.types.integration_tags_list

        out["tags"] = aws_sdk_glue.types.integration_tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "Status" in data:
        import aws_sdk_glue.types.integration_status

        out["status"] = aws_sdk_glue.types.integration_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        raise DeserializationError("ModifyIntegrationResponse.status required")
    if "CreateTime" in data:
        import aws_sdk_glue.types.integration_timestamp

        out["create_time"] = (
            aws_sdk_glue.types.integration_timestamp.deserialize_aws_json_1_1(
                data["CreateTime"]
            )
        )
    else:
        raise DeserializationError("ModifyIntegrationResponse.create_time required")
    if "Errors" in data:
        import aws_sdk_glue.types.integration_error_list

        out["errors"] = (
            aws_sdk_glue.types.integration_error_list.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    if "DataFilter" in data:
        out["data_filter"] = data["DataFilter"]
    if "IntegrationConfig" in data:
        import aws_sdk_glue.types.integration_config

        out["integration_config"] = (
            aws_sdk_glue.types.integration_config.deserialize_aws_json_1_1(
                data["IntegrationConfig"]
            )
        )
    return out
