"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ApplicationDependencySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string


class ApplicationDependencySummary(TypedDict, closed=True):
    application_id: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the nested application.</p>"""
    semantic_version: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the nested application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationDependencySummary) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "semantic_version" in value:
        out["semanticVersion"] = value["semantic_version"]
    return out


def deserialize_json(data: dict) -> ApplicationDependencySummary:
    out: ApplicationDependencySummary = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    return out
