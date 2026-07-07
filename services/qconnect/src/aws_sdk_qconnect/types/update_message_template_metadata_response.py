"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateMessageTemplateMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_data


class UpdateMessageTemplateMetadataResponse(TypedDict, closed=True):
    message_template: NotRequired[
        "aws_sdk_qconnect.types.message_template_data.MessageTemplateData"
    ]
    """<p>The message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMessageTemplateMetadataResponse) -> dict:
    out: dict = {}
    if "message_template" in value:
        import aws_sdk_qconnect.types.message_template_data

        out["messageTemplate"] = (
            aws_sdk_qconnect.types.message_template_data.serialize_json(
                value["message_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMessageTemplateMetadataResponse:
    out: UpdateMessageTemplateMetadataResponse = {}  # type: ignore[typeddict-item]
    if "messageTemplate" in data:
        import aws_sdk_qconnect.types.message_template_data

        out["message_template"] = (
            aws_sdk_qconnect.types.message_template_data.deserialize_json(
                data["messageTemplate"]
            )
        )
    return out
