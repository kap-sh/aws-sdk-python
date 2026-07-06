"""Generated from Smithy shape ``com.amazonaws.databrew#ListProjectsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.next_token
    import aws_sdk_databrew.types.project_list


class ListProjectsResponse(TypedDict, closed=True):
    projects: "aws_sdk_databrew.types.project_list.ProjectList"
    """<p>A list of projects that are defined .</p>"""
    next_token: NotRequired["aws_sdk_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectsResponse) -> dict:
    out: dict = {}
    import aws_sdk_databrew.types.project_list

    out["Projects"] = aws_sdk_databrew.types.project_list.serialize_json(
        value["projects"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProjectsResponse:
    out: ListProjectsResponse = {}  # type: ignore[typeddict-item]
    if "Projects" in data:
        import aws_sdk_databrew.types.project_list

        out["projects"] = aws_sdk_databrew.types.project_list.deserialize_json(
            data["Projects"]
        )
    else:
        raise DeserializationError("ListProjectsResponse.projects required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
