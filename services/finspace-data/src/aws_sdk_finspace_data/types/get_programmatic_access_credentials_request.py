"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetProgrammaticAccessCredentialsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.id_type
    import aws_sdk_finspace_data.types.session_duration


class GetProgrammaticAccessCredentialsRequest(TypedDict):
    duration_in_minutes: NotRequired[
        "aws_sdk_finspace_data.types.session_duration.SessionDuration"
    ]
    """<p>The time duration in which the credentials remain valid. </p>"""
    environment_id: "aws_sdk_finspace_data.types.id_type.IdType"
    """<p>The FinSpace environment identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProgrammaticAccessCredentialsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProgrammaticAccessCredentialsRequest:
    out: GetProgrammaticAccessCredentialsRequest = {}  # type: ignore[typeddict-item]
    return out
