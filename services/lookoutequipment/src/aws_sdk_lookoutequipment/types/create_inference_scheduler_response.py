"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateInferenceSchedulerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_scheduler_arn
    import aws_sdk_lookoutequipment.types.inference_scheduler_name
    import aws_sdk_lookoutequipment.types.inference_scheduler_status
    import aws_sdk_lookoutequipment.types.model_quality


class CreateInferenceSchedulerResponse(TypedDict, closed=True):
    inference_scheduler_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_arn.InferenceSchedulerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the inference scheduler being created. </p>"""
    inference_scheduler_name: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_name.InferenceSchedulerName"
    ]
    """<p>The name of inference scheduler being created. </p>"""
    status: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_status.InferenceSchedulerStatus"
    ]
    """<p>Indicates the status of the <code>CreateInferenceScheduler</code> operation. </p>"""
    model_quality: NotRequired[
        "aws_sdk_lookoutequipment.types.model_quality.ModelQuality"
    ]
    r"""<p>Provides a quality assessment for a model that uses labels. If Lookout for Equipment determines that the model quality is poor based on training metrics, the value is <code>POOR_QUALITY_DETECTED</code>. Otherwise, the value is <code>QUALITY_THRESHOLD_MET</code>. </p> <p>If the model is unlabeled, the model quality can't be assessed and the value of <code>ModelQuality</code> is <code>CANNOT_DETERMINE_QUALITY</code>. In this situation, you can get a model quality assessment by adding labels to the input dataset and retraining the model.</p> <p>For information about using labels with your models, see <a href=\"https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-labeling.html\">Understanding labeling</a>.</p> <p>For information about improving the quality of a model, see <a href=\"https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/best-practices.html\">Best practices with Amazon Lookout for Equipment</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateInferenceSchedulerResponse) -> dict:
    out: dict = {}
    if "inference_scheduler_arn" in value:
        out["InferenceSchedulerArn"] = value["inference_scheduler_arn"]
    if "inference_scheduler_name" in value:
        out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    if "status" in value:
        import aws_sdk_lookoutequipment.types.inference_scheduler_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.inference_scheduler_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "model_quality" in value:
        import aws_sdk_lookoutequipment.types.model_quality

        out["ModelQuality"] = (
            aws_sdk_lookoutequipment.types.model_quality.serialize_aws_json_1_0(
                value["model_quality"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateInferenceSchedulerResponse:
    out: CreateInferenceSchedulerResponse = {}  # type: ignore[typeddict-item]
    if "InferenceSchedulerArn" in data:
        out["inference_scheduler_arn"] = data["InferenceSchedulerArn"]
    if "InferenceSchedulerName" in data:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.inference_scheduler_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.inference_scheduler_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "ModelQuality" in data:
        import aws_sdk_lookoutequipment.types.model_quality

        out["model_quality"] = (
            aws_sdk_lookoutequipment.types.model_quality.deserialize_aws_json_1_0(
                data["ModelQuality"]
            )
        )
    return out
