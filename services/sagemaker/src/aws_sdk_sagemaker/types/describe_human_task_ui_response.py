"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeHumanTaskUiResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.human_task_ui_arn
    import aws_sdk_sagemaker.types.human_task_ui_name
    import aws_sdk_sagemaker.types.human_task_ui_status
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.ui_template_info


class DescribeHumanTaskUiResponse(TypedDict, closed=True):
    human_task_ui_arn: NotRequired[
        "aws_sdk_sagemaker.types.human_task_ui_arn.HumanTaskUiArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the human task user interface (worker task template).</p>"""
    human_task_ui_name: NotRequired[
        "aws_sdk_sagemaker.types.human_task_ui_name.HumanTaskUiName"
    ]
    """<p>The name of the human task user interface (worker task template).</p>"""
    human_task_ui_status: NotRequired[
        "aws_sdk_sagemaker.types.human_task_ui_status.HumanTaskUiStatus"
    ]
    """<p>The status of the human task user interface (worker task template). Valid values are listed below.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the human task user interface was created.</p>"""
    ui_template: NotRequired["aws_sdk_sagemaker.types.ui_template_info.UiTemplateInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHumanTaskUiResponse) -> dict:
    out: dict = {}
    if "human_task_ui_arn" in value:
        out["HumanTaskUiArn"] = value["human_task_ui_arn"]
    if "human_task_ui_name" in value:
        out["HumanTaskUiName"] = value["human_task_ui_name"]
    if "human_task_ui_status" in value:
        import aws_sdk_sagemaker.types.human_task_ui_status

        out["HumanTaskUiStatus"] = (
            aws_sdk_sagemaker.types.human_task_ui_status.serialize_aws_json_1_1(
                value["human_task_ui_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "ui_template" in value:
        import aws_sdk_sagemaker.types.ui_template_info

        out["UiTemplate"] = (
            aws_sdk_sagemaker.types.ui_template_info.serialize_aws_json_1_1(
                value["ui_template"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHumanTaskUiResponse:
    out: DescribeHumanTaskUiResponse = {}  # type: ignore[typeddict-item]
    if "HumanTaskUiArn" in data:
        out["human_task_ui_arn"] = data["HumanTaskUiArn"]
    if "HumanTaskUiName" in data:
        out["human_task_ui_name"] = data["HumanTaskUiName"]
    if "HumanTaskUiStatus" in data:
        import aws_sdk_sagemaker.types.human_task_ui_status

        out["human_task_ui_status"] = (
            aws_sdk_sagemaker.types.human_task_ui_status.deserialize_aws_json_1_1(
                data["HumanTaskUiStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "UiTemplate" in data:
        import aws_sdk_sagemaker.types.ui_template_info

        out["ui_template"] = (
            aws_sdk_sagemaker.types.ui_template_info.deserialize_aws_json_1_1(
                data["UiTemplate"]
            )
        )
    return out
