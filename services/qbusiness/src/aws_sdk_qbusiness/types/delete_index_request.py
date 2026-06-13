"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.index_id


class DeleteIndexRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application the Amazon Q Business index is linked to.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the Amazon Q Business index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIndexRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIndexRequest:
    out: DeleteIndexRequest = {}  # type: ignore[typeddict-item]
    return out
