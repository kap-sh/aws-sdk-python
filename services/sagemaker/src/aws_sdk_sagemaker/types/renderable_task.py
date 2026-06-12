"""Generated from Smithy shape ``com.amazonaws.sagemaker#RenderableTask``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.task_input


class RenderableTask(TypedDict):
    input: NotRequired["aws_sdk_sagemaker.types.task_input.TaskInput"]
    """<p>A JSON object that contains values for the variables defined in the template. It is made available to the template under the substitution variable <code>task.input</code>. For example, if you define a variable <code>task.input.text</code> in your template, you can supply the variable in the JSON object as <code>\"text\": \"sample text\"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenderableTask) -> dict:
    out: dict = {}
    if "input" in value:
        out["Input"] = value["input"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RenderableTask:
    out: RenderableTask = {}  # type: ignore[typeddict-item]
    if "Input" in data:
        out["input"] = data["Input"]
    return out
