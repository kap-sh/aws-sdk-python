"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateSourceRepositoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.source_repository_description_string
    import capo_codecatalyst.types.source_repository_name_string


class CreateSourceRepositoryResponse(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the source repository.</p>"""
    description: NotRequired[
        "capo_codecatalyst.types.source_repository_description_string.SourceRepositoryDescriptionString"
    ]
    """<p>The description of the source repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSourceRepositoryResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateSourceRepositoryResponse:
    out: CreateSourceRepositoryResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("CreateSourceRepositoryResponse.space_name required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError(
            "CreateSourceRepositoryResponse.project_name required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSourceRepositoryResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    return out
