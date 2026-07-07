"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#StartRetrainingSchedulerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.model_arn
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.retraining_scheduler_status


class StartRetrainingSchedulerResponse(TypedDict, closed=True):
    model_name: NotRequired["aws_sdk_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the model whose retraining scheduler is being started. </p>"""
    model_arn: NotRequired["aws_sdk_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The ARN of the model whose retraining scheduler is being started. </p>"""
    status: NotRequired[
        "aws_sdk_lookoutequipment.types.retraining_scheduler_status.RetrainingSchedulerStatus"
    ]
    """<p>The status of the retraining scheduler. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartRetrainingSchedulerResponse) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "status" in value:
        import aws_sdk_lookoutequipment.types.retraining_scheduler_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.retraining_scheduler_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartRetrainingSchedulerResponse:
    out: StartRetrainingSchedulerResponse = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.retraining_scheduler_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.retraining_scheduler_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
