"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteNotebookInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_name


class DeleteNotebookInstanceInput(TypedDict, closed=True):
    notebook_instance_name: NotRequired[
        "capo_sagemaker.types.notebook_instance_name.NotebookInstanceName"
    ]
    """<p>The name of the SageMaker AI notebook instance to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNotebookInstanceInput) -> dict:
    out: dict = {}
    if "notebook_instance_name" in value:
        out["NotebookInstanceName"] = value["notebook_instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNotebookInstanceInput:
    out: DeleteNotebookInstanceInput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceName" in data:
        out["notebook_instance_name"] = data["NotebookInstanceName"]
    return out
