"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.index_id


class GetIndexRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application connected to the index.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the Amazon Q Business index you want information on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIndexRequest:
    out: GetIndexRequest = {}  # type: ignore[typeddict-item]
    return out
