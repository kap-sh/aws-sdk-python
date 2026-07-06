"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelPackageGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_package_group_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListModelPackageGroupsOutput(TypedDict, closed=True):
    model_package_group_summary_list: NotRequired[
        "aws_sdk_sagemaker.types.model_package_group_summary_list.ModelPackageGroupSummaryList"
    ]
    """<p>A list of summaries of the model groups in your Amazon Web Services account.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of model groups, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelPackageGroupsOutput) -> dict:
    out: dict = {}
    if "model_package_group_summary_list" in value:
        import aws_sdk_sagemaker.types.model_package_group_summary_list

        out["ModelPackageGroupSummaryList"] = (
            aws_sdk_sagemaker.types.model_package_group_summary_list.serialize_aws_json_1_1(
                value["model_package_group_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelPackageGroupsOutput:
    out: ListModelPackageGroupsOutput = {}  # type: ignore[typeddict-item]
    if "ModelPackageGroupSummaryList" in data:
        import aws_sdk_sagemaker.types.model_package_group_summary_list

        out["model_package_group_summary_list"] = (
            aws_sdk_sagemaker.types.model_package_group_summary_list.deserialize_aws_json_1_1(
                data["ModelPackageGroupSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
