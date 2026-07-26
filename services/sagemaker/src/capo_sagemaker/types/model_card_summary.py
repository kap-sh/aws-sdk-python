"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.model_card_arn
    import capo_sagemaker.types.model_card_status
    import capo_sagemaker.types.timestamp


class ModelCardSummary(TypedDict, closed=True):
    model_card_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model card.</p>"""
    model_card_arn: NotRequired["capo_sagemaker.types.model_card_arn.ModelCardArn"]
    """<p>The Amazon Resource Name (ARN) of the model card.</p>"""
    model_card_status: NotRequired[
        "capo_sagemaker.types.model_card_status.ModelCardStatus"
    ]
    """<p>The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.</p> <ul> <li> <p> <code>Draft</code>: The model card is a work in progress.</p> </li> <li> <p> <code>PendingReview</code>: The model card is pending review.</p> </li> <li> <p> <code>Approved</code>: The model card is approved.</p> </li> <li> <p> <code>Archived</code>: The model card is archived. No more updates should be made to the model card, but it can still be exported.</p> </li> </ul>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model card was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model card was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardSummary) -> dict:
    out: dict = {}
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    if "model_card_arn" in value:
        out["ModelCardArn"] = value["model_card_arn"]
    if "model_card_status" in value:
        import capo_sagemaker.types.model_card_status

        out["ModelCardStatus"] = (
            capo_sagemaker.types.model_card_status.serialize_aws_json_1_1(
                value["model_card_status"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelCardSummary:
    out: ModelCardSummary = {}  # type: ignore[typeddict-item]
    if "ModelCardName" in data:
        out["model_card_name"] = data["ModelCardName"]
    if "ModelCardArn" in data:
        out["model_card_arn"] = data["ModelCardArn"]
    if "ModelCardStatus" in data:
        import capo_sagemaker.types.model_card_status

        out["model_card_status"] = (
            capo_sagemaker.types.model_card_status.deserialize_aws_json_1_1(
                data["ModelCardStatus"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
