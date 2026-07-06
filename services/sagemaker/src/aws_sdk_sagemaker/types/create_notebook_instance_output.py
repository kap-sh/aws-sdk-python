"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateNotebookInstanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.notebook_instance_arn


class CreateNotebookInstanceOutput(TypedDict, closed=True):
    notebook_instance_arn: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_arn.NotebookInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the notebook instance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNotebookInstanceOutput) -> dict:
    out: dict = {}
    if "notebook_instance_arn" in value:
        out["NotebookInstanceArn"] = value["notebook_instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNotebookInstanceOutput:
    out: CreateNotebookInstanceOutput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceArn" in data:
        out["notebook_instance_arn"] = data["NotebookInstanceArn"]
    return out
