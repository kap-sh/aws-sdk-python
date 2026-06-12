"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#CreateCloudFormationChangeSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string


class CreateCloudFormationChangeSetResponse(TypedDict):
    application_id: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The application Amazon Resource Name (ARN).</p>"""
    change_set_id: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the change set.</p><p>Length constraints: Minimum length of 1.</p><p>Pattern: ARN:[-a-zA-Z0-9:/]*</p>"""
    semantic_version: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the application:</p><p> <a href=\"https://semver.org/\">https://semver.org/</a> </p>"""
    stack_id: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The unique ID of the stack.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCloudFormationChangeSetResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "change_set_id" in value:
        out["changeSetId"] = value["change_set_id"]
    if "semantic_version" in value:
        out["semanticVersion"] = value["semantic_version"]
    if "stack_id" in value:
        out["stackId"] = value["stack_id"]
    return out


def deserialize_json(data: dict) -> CreateCloudFormationChangeSetResponse:
    out: CreateCloudFormationChangeSetResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "changeSetId" in data:
        out["change_set_id"] = data["changeSetId"]
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    if "stackId" in data:
        out["stack_id"] = data["stackId"]
    return out
