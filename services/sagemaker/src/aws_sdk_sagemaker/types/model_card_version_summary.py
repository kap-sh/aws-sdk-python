"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.model_card_arn
    import aws_sdk_sagemaker.types.model_card_status
    import aws_sdk_sagemaker.types.timestamp


class ModelCardVersionSummary(TypedDict, closed=True):
    model_card_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model card.</p>"""
    model_card_arn: NotRequired["aws_sdk_sagemaker.types.model_card_arn.ModelCardArn"]
    """<p>The Amazon Resource Name (ARN) of the model card.</p>"""
    model_card_status: NotRequired[
        "aws_sdk_sagemaker.types.model_card_status.ModelCardStatus"
    ]
    """<p>The approval status of the model card version within your organization. Different organizations might have different criteria for model card review and approval.</p> <ul> <li> <p> <code>Draft</code>: The model card is a work in progress.</p> </li> <li> <p> <code>PendingReview</code>: The model card is pending review.</p> </li> <li> <p> <code>Approved</code>: The model card is approved.</p> </li> <li> <p> <code>Archived</code>: The model card is archived. No more updates should be made to the model card, but it can still be exported.</p> </li> </ul>"""
    model_card_version: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>A version of the model card.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model card version was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time date and time that the model card version was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardVersionSummary) -> dict:
    out: dict = {}
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    if "model_card_arn" in value:
        out["ModelCardArn"] = value["model_card_arn"]
    if "model_card_status" in value:
        import aws_sdk_sagemaker.types.model_card_status

        out["ModelCardStatus"] = (
            aws_sdk_sagemaker.types.model_card_status.serialize_aws_json_1_1(
                value["model_card_status"]
            )
        )
    if "model_card_version" in value:
        out["ModelCardVersion"] = value["model_card_version"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelCardVersionSummary:
    out: ModelCardVersionSummary = {}  # type: ignore[typeddict-item]
    if "ModelCardName" in data:
        out["model_card_name"] = data["ModelCardName"]
    if "ModelCardArn" in data:
        out["model_card_arn"] = data["ModelCardArn"]
    if "ModelCardStatus" in data:
        import aws_sdk_sagemaker.types.model_card_status

        out["model_card_status"] = (
            aws_sdk_sagemaker.types.model_card_status.deserialize_aws_json_1_1(
                data["ModelCardStatus"]
            )
        )
    if "ModelCardVersion" in data:
        out["model_card_version"] = data["ModelCardVersion"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
