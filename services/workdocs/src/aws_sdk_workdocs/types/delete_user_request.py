"""Generated from Smithy shape ``com.amazonaws.workdocs#DeleteUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.id_type


class DeleteUserRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using Amazon Web Services credentials.</p>"""
    user_id: "aws_sdk_workdocs.types.id_type.IdType"
    """<p>The ID of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
    return out
