"""Generated from Smithy shape ``com.amazonaws.qbusiness#DisassociatePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.string


class DisassociatePermissionRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application.</p>"""
    statement_id: "aws_sdk_qbusiness.types.string.String"
    """<p>The statement ID of the permission to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociatePermissionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociatePermissionRequest:
    out: DisassociatePermissionRequest = {}  # type: ignore[typeddict-item]
    return out
