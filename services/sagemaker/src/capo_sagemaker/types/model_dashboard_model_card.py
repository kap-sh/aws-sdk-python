"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDashboardModelCard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.model_card_arn
    import capo_sagemaker.types.model_card_security_config
    import capo_sagemaker.types.model_card_status
    import capo_sagemaker.types.string
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class ModelDashboardModelCard(TypedDict, closed=True):
    model_card_arn: NotRequired["capo_sagemaker.types.model_card_arn.ModelCardArn"]
    """<p>The Amazon Resource Name (ARN) for a model card.</p>"""
    model_card_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of a model card.</p>"""
    model_card_version: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The model card version.</p>"""
    model_card_status: NotRequired[
        "capo_sagemaker.types.model_card_status.ModelCardStatus"
    ]
    """<p>The model card status.</p>"""
    security_config: NotRequired[
        "capo_sagemaker.types.model_card_security_config.ModelCardSecurityConfig"
    ]
    """<p>The KMS Key ID (<code>KMSKeyId</code>) for encryption of model card information.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the model card was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the model card was last updated.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The tags associated with a model card.</p>"""
    model_id: NotRequired["capo_sagemaker.types.string.String"]
    """<p>For models created in SageMaker, this is the model ARN. For models created outside of SageMaker, this is a user-customized string.</p>"""
    risk_rating: NotRequired["capo_sagemaker.types.string.String"]
    """<p>A model card's risk rating. Can be low, medium, or high.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDashboardModelCard) -> dict:
    out: dict = {}
    if "model_card_arn" in value:
        out["ModelCardArn"] = value["model_card_arn"]
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    if "model_card_version" in value:
        out["ModelCardVersion"] = value["model_card_version"]
    if "model_card_status" in value:
        import capo_sagemaker.types.model_card_status

        out["ModelCardStatus"] = (
            capo_sagemaker.types.model_card_status.serialize_aws_json_1_1(
                value["model_card_status"]
            )
        )
    if "security_config" in value:
        import capo_sagemaker.types.model_card_security_config

        out["SecurityConfig"] = (
            capo_sagemaker.types.model_card_security_config.serialize_aws_json_1_1(
                value["security_config"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "model_id" in value:
        out["ModelId"] = value["model_id"]
    if "risk_rating" in value:
        out["RiskRating"] = value["risk_rating"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelDashboardModelCard:
    out: ModelDashboardModelCard = {}  # type: ignore[typeddict-item]
    if "ModelCardArn" in data:
        out["model_card_arn"] = data["ModelCardArn"]
    if "ModelCardName" in data:
        out["model_card_name"] = data["ModelCardName"]
    if "ModelCardVersion" in data:
        out["model_card_version"] = data["ModelCardVersion"]
    if "ModelCardStatus" in data:
        import capo_sagemaker.types.model_card_status

        out["model_card_status"] = (
            capo_sagemaker.types.model_card_status.deserialize_aws_json_1_1(
                data["ModelCardStatus"]
            )
        )
    if "SecurityConfig" in data:
        import capo_sagemaker.types.model_card_security_config

        out["security_config"] = (
            capo_sagemaker.types.model_card_security_config.deserialize_aws_json_1_1(
                data["SecurityConfig"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "CreatedBy" in data:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ModelId" in data:
        out["model_id"] = data["ModelId"]
    if "RiskRating" in data:
        out["risk_rating"] = data["RiskRating"]
    return out
