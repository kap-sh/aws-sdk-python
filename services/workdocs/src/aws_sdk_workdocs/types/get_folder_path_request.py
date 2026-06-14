"""Generated from Smithy shape ``com.amazonaws.workdocs#GetFolderPathRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.field_names_type
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.limit_type
    import aws_sdk_workdocs.types.page_marker_type


class GetFolderPathRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    folder_id: "aws_sdk_workdocs.types.id_type.IdType"
    """<p>The ID of the folder.</p>"""
    limit: NotRequired["aws_sdk_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of levels in the hierarchy to return.</p>"""
    fields: NotRequired["aws_sdk_workdocs.types.field_names_type.FieldNamesType"]
    r"""<p>A comma-separated list of values. Specify \"NAME\" to include the names of the parent folders.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>This value is not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFolderPathRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFolderPathRequest:
    out: GetFolderPathRequest = {}  # type: ignore[typeddict-item]
    return out
