"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.date
    import aws_sdk_databrew.types.project_name


class UpdateProjectResponse(TypedDict, closed=True):
    last_modified_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the project was last modified.</p>"""
    name: "aws_sdk_databrew.types.project_name.ProjectName"
    """<p>The name of the project that you updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectResponse) -> dict:
    out: dict = {}
    if "last_modified_date" in value:
        import aws_sdk_databrew.types.date

        out["LastModifiedDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateProjectResponse:
    out: UpdateProjectResponse = {}  # type: ignore[typeddict-item]
    if "LastModifiedDate" in data:
        import aws_sdk_databrew.types.date

        out["last_modified_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateProjectResponse.name required")
    return out
