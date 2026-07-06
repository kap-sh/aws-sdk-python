"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteChatControlsConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id


class DeleteChatControlsConfigurationRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application the chat controls have been configured for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChatControlsConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChatControlsConfigurationRequest:
    out: DeleteChatControlsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
