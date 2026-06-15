"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCard``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.model_card_arn
    import aws_sdk_sagemaker.types.model_card_content
    import aws_sdk_sagemaker.types.model_card_security_config
    import aws_sdk_sagemaker.types.model_card_status
    import aws_sdk_sagemaker.types.string
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.user_context


class ModelCard(TypedDict):
    model_card_arn: NotRequired["aws_sdk_sagemaker.types.model_card_arn.ModelCardArn"]
    """<p>The Amazon Resource Name (ARN) of the model card.</p>"""
    model_card_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The unique name of the model card.</p>"""
    model_card_version: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The version of the model card.</p>"""
    content: NotRequired["aws_sdk_sagemaker.types.model_card_content.ModelCardContent"]
    r"""<p>The content of the model card. Content uses the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema\">model card JSON schema</a> and provided as a string.</p>"""
    model_card_status: NotRequired[
        "aws_sdk_sagemaker.types.model_card_status.ModelCardStatus"
    ]
    """<p>The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.</p> <ul> <li> <p> <code>Draft</code>: The model card is a work in progress.</p> </li> <li> <p> <code>PendingReview</code>: The model card is pending review.</p> </li> <li> <p> <code>Approved</code>: The model card is approved.</p> </li> <li> <p> <code>Archived</code>: The model card is archived. No more updates should be made to the model card, but it can still be exported.</p> </li> </ul>"""
    security_config: NotRequired[
        "aws_sdk_sagemaker.types.model_card_security_config.ModelCardSecurityConfig"
    ]
    """<p>The security configuration used to protect model card data.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model card was created.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model card was last modified.</p>"""
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>Key-value pairs used to manage metadata for the model card.</p>"""
    model_id: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The unique name (ID) of the model.</p>"""
    risk_rating: NotRequired["aws_sdk_sagemaker.types.string.String"]
    r"""<p>The risk rating of the model. Different organizations might have different criteria for model card risk ratings. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-risk-rating.html\">Risk ratings</a>.</p>"""
    model_package_group_name: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The model package group that contains the model package. Only relevant for model cards created for model packages in the Amazon SageMaker Model Registry. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCard) -> dict:
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
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "model_id" in value:
        out["ModelId"] = value["model_id"]
    if "risk_rating" in value:
        out["RiskRating"] = value["risk_rating"]
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelCard:
    out: ModelCard = {}  # type: ignore[typeddict-item]
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
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ModelId" in data:
        out["model_id"] = data["ModelId"]
    if "RiskRating" in data:
        out["risk_rating"] = data["RiskRating"]
    if "ModelPackageGroupName" in data:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    return out
