"""Generated from Smithy shape ``com.amazonaws.qconnect#GetContentSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uuid_or_arn


class GetContentSummaryRequest(TypedDict, closed=True):
    content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContentSummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContentSummaryRequest:
    out: GetContentSummaryRequest = {}  # type: ignore[typeddict-item]
    return out
