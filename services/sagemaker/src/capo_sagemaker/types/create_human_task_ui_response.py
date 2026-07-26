"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateHumanTaskUiResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.human_task_ui_arn


class CreateHumanTaskUiResponse(TypedDict, closed=True):
    human_task_ui_arn: NotRequired[
        "capo_sagemaker.types.human_task_ui_arn.HumanTaskUiArn"
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
