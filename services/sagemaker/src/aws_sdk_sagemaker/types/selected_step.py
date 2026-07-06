"""Generated from Smithy shape ``com.amazonaws.sagemaker#SelectedStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string256


class SelectedStep(TypedDict, closed=True):
    step_name: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The name of the pipeline step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectedStep) -> dict:
    out: dict = {}
    if "step_name" in value:
        out["StepName"] = value["step_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SelectedStep:
    out: SelectedStep = {}  # type: ignore[typeddict-item]
    if "StepName" in data:
        out["step_name"] = data["StepName"]
    return out
