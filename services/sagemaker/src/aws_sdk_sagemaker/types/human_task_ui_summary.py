"""Generated from Smithy shape ``com.amazonaws.sagemaker#HumanTaskUiSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.human_task_ui_arn
    import aws_sdk_sagemaker.types.human_task_ui_name
    import aws_sdk_sagemaker.types.timestamp


class HumanTaskUiSummary(TypedDict):
    human_task_ui_name: NotRequired[
        "aws_sdk_sagemaker.types.human_task_ui_name.HumanTaskUiName"
    ]
    """<p>The name of the human task user interface.</p>"""
    human_task_ui_arn: NotRequired[
        "aws_sdk_sagemaker.types.human_task_ui_arn.HumanTaskUiArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the human task user interface.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp when SageMaker created the human task user interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanTaskUiSummary) -> dict:
    out: dict = {}
    if "human_task_ui_name" in value:
        out["HumanTaskUiName"] = value["human_task_ui_name"]
    if "human_task_ui_arn" in value:
        out["HumanTaskUiArn"] = value["human_task_ui_arn"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanTaskUiSummary:
    out: HumanTaskUiSummary = {}  # type: ignore[typeddict-item]
    if "HumanTaskUiName" in data:
        out["human_task_ui_name"] = data["HumanTaskUiName"]
    if "HumanTaskUiArn" in data:
        out["human_task_ui_arn"] = data["HumanTaskUiArn"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
