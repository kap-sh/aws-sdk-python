"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeHumanTaskUiRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.human_task_ui_name


class DescribeHumanTaskUiRequest(TypedDict):
    human_task_ui_name: NotRequired[
        "aws_sdk_sagemaker.types.human_task_ui_name.HumanTaskUiName"
    ]
    """<p>The name of the human task user interface (worker task template) you want information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHumanTaskUiRequest) -> dict:
    out: dict = {}
    if "human_task_ui_name" in value:
        out["HumanTaskUiName"] = value["human_task_ui_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHumanTaskUiRequest:
    out: DescribeHumanTaskUiRequest = {}  # type: ignore[typeddict-item]
    if "HumanTaskUiName" in data:
        out["human_task_ui_name"] = data["HumanTaskUiName"]
    return out
