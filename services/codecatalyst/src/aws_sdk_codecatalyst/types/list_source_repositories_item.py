"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListSourceRepositoriesItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.source_repository_description_string
    import aws_sdk_codecatalyst.types.source_repository_id_string
    import aws_sdk_codecatalyst.types.source_repository_name_string
    import aws_sdk_codecatalyst.types.timestamp


class ListSourceRepositoriesItem(TypedDict):
    id: "aws_sdk_codecatalyst.types.source_repository_id_string.SourceRepositoryIdString"
    """<p>The system-generated unique ID of the source repository.</p>"""
    name: "aws_sdk_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the source repository.</p>"""
    description: NotRequired[
        "aws_sdk_codecatalyst.types.source_repository_description_string.SourceRepositoryDescriptionString"
    ]
    """<p>The description of the repository, if any.</p>"""
    last_updated_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The time the source repository was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""
    created_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The time the source repository was created, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceRepositoriesItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
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


def deserialize_json(data: dict) -> ListSourceRepositoriesItem:
    out: ListSourceRepositoriesItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ListSourceRepositoriesItem.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ListSourceRepositoriesItem.name required")
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
            "ListSourceRepositoriesItem.last_updated_time required"
        )
    if "createdTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["created_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    else:
        raise DeserializationError("ListSourceRepositoriesItem.created_time required")
    return out
