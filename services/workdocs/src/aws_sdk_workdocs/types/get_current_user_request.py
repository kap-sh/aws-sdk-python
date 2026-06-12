"""Generated from Smithy shape ``com.amazonaws.workdocs#GetCurrentUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type


class GetCurrentUserRequest(TypedDict):
    authentication_token: (
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    )
    """<p>Amazon WorkDocs authentication token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCurrentUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCurrentUserRequest:
    out: GetCurrentUserRequest = {}  # type: ignore[typeddict-item]
    return out
