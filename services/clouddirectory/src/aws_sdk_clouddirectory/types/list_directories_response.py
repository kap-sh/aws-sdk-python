"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListDirectoriesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.directory_list
    import aws_sdk_clouddirectory.types.next_token


class ListDirectoriesResponse(TypedDict):
    directories: "aws_sdk_clouddirectory.types.directory_list.DirectoryList"
    """<p>Lists all directories that are associated with your account in pagination fashion.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDirectoriesResponse) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.directory_list

    out["Directories"] = aws_sdk_clouddirectory.types.directory_list.serialize_json(
        value["directories"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDirectoriesResponse:
    out: ListDirectoriesResponse = {}  # type: ignore[typeddict-item]
    if "Directories" in data:
        import aws_sdk_clouddirectory.types.directory_list

        out["directories"] = (
            aws_sdk_clouddirectory.types.directory_list.deserialize_json(
                data["Directories"]
            )
        )
    else:
        raise DeserializationError("ListDirectoriesResponse.directories required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
