"""Generated from Smithy shape ``com.amazonaws.qconnect#GetAssistantRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid_or_arn


class GetAssistantRequest(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssistantRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssistantRequest:
    out: GetAssistantRequest = {}  # type: ignore[typeddict-item]
    return out
