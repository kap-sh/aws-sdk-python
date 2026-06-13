"""Generated from Smithy shape ``com.amazonaws.wisdom#DeleteAssistantRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.uuid_or_arn


class DeleteAssistantRequest(TypedDict):
    assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssistantRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssistantRequest:
    out: DeleteAssistantRequest = {}  # type: ignore[typeddict-item]
    return out
