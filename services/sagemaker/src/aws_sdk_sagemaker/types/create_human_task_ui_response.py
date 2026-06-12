"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateHumanTaskUiResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.human_task_ui_arn


class CreateHumanTaskUiResponse(TypedDict):
    human_task_ui_arn: NotRequired[
        "aws_sdk_sagemaker.types.human_task_ui_arn.HumanTaskUiArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the human review workflow user interface you create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHumanTaskUiResponse) -> dict:
    out: dict = {}
    if "human_task_ui_arn" in value:
        out["HumanTaskUiArn"] = value["human_task_ui_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHumanTaskUiResponse:
    out: CreateHumanTaskUiResponse = {}  # type: ignore[typeddict-item]
    if "HumanTaskUiArn" in data:
        out["human_task_ui_arn"] = data["HumanTaskUiArn"]
    return out
