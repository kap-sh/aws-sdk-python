"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePresignedNotebookInstanceUrlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_name
    import capo_sagemaker.types.session_expiration_duration_in_seconds


class CreatePresignedNotebookInstanceUrlInput(TypedDict, closed=True):
    notebook_instance_name: NotRequired[
        "capo_sagemaker.types.notebook_instance_name.NotebookInstanceName"
    ]
    """<p>The name of the notebook instance.</p>"""
    session_expiration_duration_in_seconds: NotRequired[
        "capo_sagemaker.types.session_expiration_duration_in_seconds.SessionExpirationDurationInSeconds"
    ]
    """<p>The duration of the session, in seconds. The default is 12 hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePresignedNotebookInstanceUrlInput) -> dict:
    out: dict = {}
    if "notebook_instance_name" in value:
        out["NotebookInstanceName"] = value["notebook_instance_name"]
    if "session_expiration_duration_in_seconds" in value:
        out["SessionExpirationDurationInSeconds"] = value[
            "session_expiration_duration_in_seconds"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePresignedNotebookInstanceUrlInput:
    out: CreatePresignedNotebookInstanceUrlInput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceName" in data:
        out["notebook_instance_name"] = data["NotebookInstanceName"]
    if "SessionExpirationDurationInSeconds" in data:
        out["session_expiration_duration_in_seconds"] = data[
            "SessionExpirationDurationInSeconds"
        ]
    return out
