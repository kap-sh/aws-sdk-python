"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#StopInferenceSchedulerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.inference_scheduler_arn
    import capo_lookoutequipment.types.inference_scheduler_name
    import capo_lookoutequipment.types.inference_scheduler_status
    import capo_lookoutequipment.types.model_arn
    import capo_lookoutequipment.types.model_name


class StopInferenceSchedulerResponse(TypedDict, closed=True):
    model_arn: NotRequired["capo_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the machine learning model used by the inference scheduler being stopped. </p>"""
    model_name: NotRequired["capo_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the machine learning model used by the inference scheduler being stopped. </p>"""
    inference_scheduler_name: NotRequired[
        "capo_lookoutequipment.types.inference_scheduler_name.InferenceSchedulerName"
    ]
    """<p>The name of the inference scheduler being stopped. </p>"""
    inference_scheduler_arn: NotRequired[
        "capo_lookoutequipment.types.inference_scheduler_arn.InferenceSchedulerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the inference schedule being stopped. </p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.inference_scheduler_status.InferenceSchedulerStatus"
    ]
    """<p>Indicates the status of the inference scheduler. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopInferenceSchedulerResponse) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "inference_scheduler_name" in value:
        out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    if "inference_scheduler_arn" in value:
        out["InferenceSchedulerArn"] = value["inference_scheduler_arn"]
    if "status" in value:
        import capo_lookoutequipment.types.inference_scheduler_status

        out["Status"] = (
            capo_lookoutequipment.types.inference_scheduler_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StopInferenceSchedulerResponse:
    out: StopInferenceSchedulerResponse = {}  # type: ignore[typeddict-item]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "InferenceSchedulerName" in data:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    if "InferenceSchedulerArn" in data:
        out["inference_scheduler_arn"] = data["InferenceSchedulerArn"]
    if "Status" in data:
        import capo_lookoutequipment.types.inference_scheduler_status

        out["status"] = (
            capo_lookoutequipment.types.inference_scheduler_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
