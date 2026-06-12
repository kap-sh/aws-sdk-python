"""Generated from Smithy shape ``com.amazonaws.workdocs#DeleteFolderContentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.resource_id_type


class DeleteFolderContentsRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFolderContentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFolderContentsRequest:
    out: DeleteFolderContentsRequest = {}  # type: ignore[typeddict-item]
    return out
