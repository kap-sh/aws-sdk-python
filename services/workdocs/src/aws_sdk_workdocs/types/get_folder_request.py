"""Generated from Smithy shape ``com.amazonaws.workdocs#GetFolderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.boolean_type
    import aws_sdk_workdocs.types.resource_id_type


class GetFolderRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the folder.</p>"""
    include_custom_metadata: "aws_sdk_workdocs.types.boolean_type.BooleanType"
    """<p>Set to TRUE to include custom metadata in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFolderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFolderRequest:
    out: GetFolderRequest = {}  # type: ignore[typeddict-item]
    return out
