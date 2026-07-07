"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetRetrieverRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.retriever_id


class GetRetrieverRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application using the retriever.</p>"""
    retriever_id: "aws_sdk_qbusiness.types.retriever_id.RetrieverId"
    """<p>The identifier of the retriever.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRetrieverRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRetrieverRequest:
    out: GetRetrieverRequest = {}  # type: ignore[typeddict-item]
    return out
