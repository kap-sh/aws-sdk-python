"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePresignedNotebookInstanceUrlOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.notebook_instance_url


class CreatePresignedNotebookInstanceUrlOutput(TypedDict):
    authorized_url: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_url.NotebookInstanceUrl"
    ]
    """<p>A JSON object that contains the URL string. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePresignedNotebookInstanceUrlOutput) -> dict:
    out: dict = {}
    if "authorized_url" in value:
        out["AuthorizedUrl"] = value["authorized_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePresignedNotebookInstanceUrlOutput:
    out: CreatePresignedNotebookInstanceUrlOutput = {}  # type: ignore[typeddict-item]
    if "AuthorizedUrl" in data:
        out["authorized_url"] = data["AuthorizedUrl"]
    return out
