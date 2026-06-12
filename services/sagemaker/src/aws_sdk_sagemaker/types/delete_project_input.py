"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteProjectInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.project_entity_name


class DeleteProjectInput(TypedDict):
    project_name: NotRequired[
        "aws_sdk_sagemaker.types.project_entity_name.ProjectEntityName"
    ]
    """<p>The name of the project to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProjectInput) -> dict:
    out: dict = {}
    if "project_name" in value:
        out["ProjectName"] = value["project_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProjectInput:
    out: DeleteProjectInput = {}  # type: ignore[typeddict-item]
    if "ProjectName" in data:
        out["project_name"] = data["ProjectName"]
    return out
