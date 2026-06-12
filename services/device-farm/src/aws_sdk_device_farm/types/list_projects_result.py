"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListProjectsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.projects


class ListProjectsResult(TypedDict):
    projects: NotRequired["aws_sdk_device_farm.types.projects.Projects"]
    """<p>Information about the projects.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProjectsResult) -> dict:
    out: dict = {}
    if "projects" in value:
        import aws_sdk_device_farm.types.projects

        out["projects"] = aws_sdk_device_farm.types.projects.serialize_aws_json_1_1(
            value["projects"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProjectsResult:
    out: ListProjectsResult = {}  # type: ignore[typeddict-item]
    if "projects" in data:
        import aws_sdk_device_farm.types.projects

        out["projects"] = aws_sdk_device_farm.types.projects.deserialize_aws_json_1_1(
            data["projects"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
