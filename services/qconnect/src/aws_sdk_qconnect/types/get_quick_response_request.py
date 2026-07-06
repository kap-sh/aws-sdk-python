"""Generated from Smithy shape ``com.amazonaws.qconnect#GetQuickResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid_or_arn


class GetQuickResponseRequest(TypedDict, closed=True):
    quick_response_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the quick response.</p>"""
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should be a QUICK_RESPONSES type knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQuickResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQuickResponseRequest:
    out: GetQuickResponseRequest = {}  # type: ignore[typeddict-item]
    return out
