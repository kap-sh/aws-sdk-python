"""Generated from Smithy shape ``com.amazonaws.qconnect#DeleteContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid_or_arn


class DeleteContentRequest(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    content_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContentRequest:
    out: DeleteContentRequest = {}  # type: ignore[typeddict-item]
    return out
