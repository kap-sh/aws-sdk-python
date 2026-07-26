"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelPackagesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_package_summary_list
    import capo_sagemaker.types.next_token


class ListModelPackagesOutput(TypedDict, closed=True):
    model_package_summary_list: NotRequired[
        "capo_sagemaker.types.model_package_summary_list.ModelPackageSummaryList"
    ]
    """<p>An array of <code>ModelPackageSummary</code> objects, each of which lists a model package.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of model packages, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelPackagesOutput) -> dict:
    out: dict = {}
    if "model_package_summary_list" in value:
        import capo_sagemaker.types.model_package_summary_list

        out["ModelPackageSummaryList"] = (
            capo_sagemaker.types.model_package_summary_list.serialize_aws_json_1_1(
                value["model_package_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelPackagesOutput:
    out: ListModelPackagesOutput = {}  # type: ignore[typeddict-item]
    if "ModelPackageSummaryList" in data:
        import capo_sagemaker.types.model_package_summary_list

        out["model_package_summary_list"] = (
            capo_sagemaker.types.model_package_summary_list.deserialize_aws_json_1_1(
                data["ModelPackageSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
