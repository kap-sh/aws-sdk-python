"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelCardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.model_card_arn
    import aws_sdk_sagemaker.types.model_card_content
    import aws_sdk_sagemaker.types.model_card_processing_status
    import aws_sdk_sagemaker.types.model_card_security_config
    import aws_sdk_sagemaker.types.model_card_status
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.user_context


class DescribeModelCardResponse(TypedDict, closed=True):
    model_card_arn: NotRequired["aws_sdk_sagemaker.types.model_card_arn.ModelCardArn"]
    """<p>The Amazon Resource Name (ARN) of the model card.</p>"""
    model_card_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model card.</p>"""
    model_card_version: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The version of the model card.</p>"""
    content: NotRequired["aws_sdk_sagemaker.types.model_card_content.ModelCardContent"]
    r"""<p>The content of the model card. Content is provided as a string in the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema\">model card JSON schema</a>.</p> <p>When you set <code>IncludedData</code> to <code>MetadataOnly</code> in the request, SageMaker returns a sanitized version of <code>Content</code> that includes only the following JSON paths, when present in the model card:</p> <ul> <li> <p> <code>model_overview.model_id</code> </p> </li> <li> <p> <code>model_overview.model_name</code> </p> </li> <li> <p> <code>intended_uses.risk_rating</code> </p> </li> <li> <p> <code>model_package_details.model_package_group_name</code> </p> </li> <li> <p> <code>model_package_details.model_package_arn</code> </p> </li> </ul> <p>All other fields are removed from <code>Content</code> when <code>IncludedData</code> is <code>MetadataOnly</code>, including model description, training details, evaluation details, business details, and additional information. To retrieve the complete <code>Content</code>, set <code>IncludedData</code> to <code>AllData</code> or omit the parameter.</p>"""
    model_card_status: NotRequired[
        "aws_sdk_sagemaker.types.model_card_status.ModelCardStatus"
    ]
    """<p>The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.</p> <ul> <li> <p> <code>Draft</code>: The model card is a work in progress.</p> </li> <li> <p> <code>PendingReview</code>: The model card is pending review.</p> </li> <li> <p> <code>Approved</code>: The model card is approved.</p> </li> <li> <p> <code>Archived</code>: The model card is archived. No more updates should be made to the model card, but it can still be exported.</p> </li> </ul>"""
    security_config: NotRequired[
        "aws_sdk_sagemaker.types.model_card_security_config.ModelCardSecurityConfig"
    ]
    """<p>The security configuration used to protect model card content.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time the model card was created.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time the model card was last modified.</p>"""
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    model_card_processing_status: NotRequired[
        "aws_sdk_sagemaker.types.model_card_processing_status.ModelCardProcessingStatus"
    ]
    """<p>The processing status of model card deletion. The <code>ModelCardProcessingStatus</code> updates throughout the different deletion steps.</p> <ul> <li> <p> <code>DeletePending</code>: Model card deletion request received.</p> </li> <li> <p> <code>DeleteInProgress</code>: Model card deletion is in progress.</p> </li> <li> <p> <code>ContentDeleted</code>: Deleted model card content.</p> </li> <li> <p> <code>ExportJobsDeleted</code>: Deleted all export jobs associated with the model card.</p> </li> <li> <p> <code>DeleteCompleted</code>: Successfully deleted the model card.</p> </li> <li> <p> <code>DeleteFailed</code>: The model card failed to delete.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelCardResponse) -> dict:
    out: dict = {}
    if "model_card_arn" in value:
        out["ModelCardArn"] = value["model_card_arn"]
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    if "model_card_version" in value:
        out["ModelCardVersion"] = value["model_card_version"]
    if "content" in value:
        out["Content"] = value["content"]
    if "model_card_status" in value:
        import aws_sdk_sagemaker.types.model_card_status

        out["ModelCardStatus"] = (
            aws_sdk_sagemaker.types.model_card_status.serialize_aws_json_1_1(
                value["model_card_status"]
            )
        )
    if "security_config" in value:
        import aws_sdk_sagemaker.types.model_card_security_config

        out["SecurityConfig"] = (
            aws_sdk_sagemaker.types.model_card_security_config.serialize_aws_json_1_1(
                value["security_config"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["CreatedBy"] = aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_modified_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "model_card_processing_status" in value:
        import aws_sdk_sagemaker.types.model_card_processing_status

        out["ModelCardProcessingStatus"] = (
            aws_sdk_sagemaker.types.model_card_processing_status.serialize_aws_json_1_1(
                value["model_card_processing_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelCardResponse:
    out: DescribeModelCardResponse = {}  # type: ignore[typeddict-item]
    if "ModelCardArn" in data:
        out["model_card_arn"] = data["ModelCardArn"]
    if "ModelCardName" in data:
        out["model_card_name"] = data["ModelCardName"]
    if "ModelCardVersion" in data:
        out["model_card_version"] = data["ModelCardVersion"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "ModelCardStatus" in data:
        import aws_sdk_sagemaker.types.model_card_status

        out["model_card_status"] = (
            aws_sdk_sagemaker.types.model_card_status.deserialize_aws_json_1_1(
                data["ModelCardStatus"]
            )
        )
    if "SecurityConfig" in data:
        import aws_sdk_sagemaker.types.model_card_security_config

        out["security_config"] = (
            aws_sdk_sagemaker.types.model_card_security_config.deserialize_aws_json_1_1(
                data["SecurityConfig"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CreatedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["created_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["CreatedBy"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["last_modified_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "ModelCardProcessingStatus" in data:
        import aws_sdk_sagemaker.types.model_card_processing_status

        out["model_card_processing_status"] = (
            aws_sdk_sagemaker.types.model_card_processing_status.deserialize_aws_json_1_1(
                data["ModelCardProcessingStatus"]
            )
        )
    return out
