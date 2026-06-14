"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetSourceRepositoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.source_repository_description_string
    import aws_sdk_codecatalyst.types.source_repository_name_string
    import aws_sdk_codecatalyst.types.timestamp


class GetSourceRepositoryResponse(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    name: "aws_sdk_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the source repository.</p>"""
    description: NotRequired[
        "aws_sdk_codecatalyst.types.source_repository_description_string.SourceRepositoryDescriptionString"
    ]
    """<p>The description of the source repository.</p>"""
    last_updated_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The time the source repository was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""
    created_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The time the source repository was created, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSourceRepositoryResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_codecatalyst.types.timestamp

    out["lastUpdatedTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    import aws_sdk_codecatalyst.types.timestamp

    out["createdTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["created_time"]
    )
    return out


def deserialize_json(data: dict) -> GetSourceRepositoryResponse:
    out: GetSourceRepositoryResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("GetSourceRepositoryResponse.space_name required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("GetSourceRepositoryResponse.project_name required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetSourceRepositoryResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "lastUpdatedTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_codecatalyst.types.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetSourceRepositoryResponse.last_updated_time required"
        )
    if "createdTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["created_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    else:
        raise DeserializationError("GetSourceRepositoryResponse.created_time required")
    return out
