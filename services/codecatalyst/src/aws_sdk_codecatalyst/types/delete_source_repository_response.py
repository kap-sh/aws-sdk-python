"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DeleteSourceRepositoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.source_repository_name_string


class DeleteSourceRepositoryResponse(TypedDict, closed=True):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    name: "aws_sdk_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSourceRepositoryResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteSourceRepositoryResponse:
    out: DeleteSourceRepositoryResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("DeleteSourceRepositoryResponse.space_name required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError(
            "DeleteSourceRepositoryResponse.project_name required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteSourceRepositoryResponse.name required")
    return out
