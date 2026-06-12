"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteDataAccessorRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_accessor_id

class DeleteDataAccessorRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application.</p>"""
    data_accessor_id: "aws_sdk_qbusiness.types.data_accessor_id.DataAccessorId"
    """<p>The unique identifier of the data accessor to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataAccessorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataAccessorRequest:
    out: DeleteDataAccessorRequest = {}  # type: ignore[typeddict-item]
    return out