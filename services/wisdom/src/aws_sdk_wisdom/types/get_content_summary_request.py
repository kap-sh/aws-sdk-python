"""Generated from Smithy shape ``com.amazonaws.wisdom#GetContentSummaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.uuid_or_arn


class GetContentSummaryRequest(TypedDict):
    content_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    knowledge_base_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContentSummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContentSummaryRequest:
    out: GetContentSummaryRequest = {}  # type: ignore[typeddict-item]
    return out
