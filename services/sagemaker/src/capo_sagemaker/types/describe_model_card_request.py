"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelCardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.included_data
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.model_card_name_or_arn


class DescribeModelCardRequest(TypedDict, closed=True):
    model_card_name: NotRequired[
        "capo_sagemaker.types.model_card_name_or_arn.ModelCardNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the model card to describe.</p>"""
    model_card_version: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The version of the model card to describe. If a version is not provided, then the latest version of the model card is described.</p>"""
    included_data: NotRequired["capo_sagemaker.types.included_data.IncludedData"]
    """<p>Specifies the level of model card data to include in the response. Use this parameter to call <code>DescribeModelCard</code> without requiring <code>kms:Decrypt</code> permission on the customer-managed Amazon Web Services KMS key.</p> <ul> <li> <p> <code>AllData</code>: Returns the full model card <code>Content</code>. This option requires <code>kms:Decrypt</code> permission on the customer-managed key, if one is associated with the model card. This is the default.</p> </li> <li> <p> <code>MetadataOnly</code>: Returns the model card with sanitized <code>Content</code> that includes only a small set of unencrypted metadata fields. This option does not require <code>kms:Decrypt</code> permission. For the list of fields preserved in the response, see <code>Content</code>.</p> </li> </ul> <p>If you don't specify a value, SageMaker returns <code>AllData</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelCardRequest) -> dict:
    out: dict = {}
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    if "model_card_version" in value:
        out["ModelCardVersion"] = value["model_card_version"]
    if "included_data" in value:
        import capo_sagemaker.types.included_data

        out["IncludedData"] = capo_sagemaker.types.included_data.serialize_aws_json_1_1(
            value["included_data"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelCardRequest:
    out: DescribeModelCardRequest = {}  # type: ignore[typeddict-item]
    if "ModelCardName" in data:
        out["model_card_name"] = data["ModelCardName"]
    if "ModelCardVersion" in data:
        out["model_card_version"] = data["ModelCardVersion"]
    if "IncludedData" in data:
        import capo_sagemaker.types.included_data

        out["included_data"] = (
            capo_sagemaker.types.included_data.deserialize_aws_json_1_1(
                data["IncludedData"]
            )
        )
    return out
