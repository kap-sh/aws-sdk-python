"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopNotebookInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_name


class StopNotebookInstanceInput(TypedDict, closed=True):
    notebook_instance_name: NotRequired[
        "capo_sagemaker.types.notebook_instance_name.NotebookInstanceName"
    ]
    """<p>The name of the notebook instance to terminate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopNotebookInstanceInput) -> dict:
    out: dict = {}
    if "notebook_instance_name" in value:
        out["NotebookInstanceName"] = value["notebook_instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopNotebookInstanceInput:
    out: StopNotebookInstanceInput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceName" in data:
        out["notebook_instance_name"] = data["NotebookInstanceName"]
    return out
