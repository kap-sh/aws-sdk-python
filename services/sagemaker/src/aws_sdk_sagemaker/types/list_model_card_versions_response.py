"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelCardVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_card_version_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListModelCardVersionsResponse(TypedDict, closed=True):
    model_card_version_summary_list: NotRequired[
        "aws_sdk_sagemaker.types.model_card_version_summary_list.ModelCardVersionSummaryList"
    ]
    """<p>The summaries of the listed versions of the model card.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of model card versions, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelCardVersionsResponse) -> dict:
    out: dict = {}
    if "model_card_version_summary_list" in value:
        import aws_sdk_sagemaker.types.model_card_version_summary_list

        out["ModelCardVersionSummaryList"] = (
            aws_sdk_sagemaker.types.model_card_version_summary_list.serialize_aws_json_1_1(
                value["model_card_version_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelCardVersionsResponse:
    out: ListModelCardVersionsResponse = {}  # type: ignore[typeddict-item]
    if "ModelCardVersionSummaryList" in data:
        import aws_sdk_sagemaker.types.model_card_version_summary_list

        out["model_card_version_summary_list"] = (
            aws_sdk_sagemaker.types.model_card_version_summary_list.deserialize_aws_json_1_1(
                data["ModelCardVersionSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
