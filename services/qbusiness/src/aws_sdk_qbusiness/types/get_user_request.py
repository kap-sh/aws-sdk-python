"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.string


class GetUserRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application connected to the user.</p>"""
    user_id: "aws_sdk_qbusiness.types.string.String"
    """<p>The user email address attached to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUserRequest:
    out: GetUserRequest = {}  # type: ignore[typeddict-item]
    return out
