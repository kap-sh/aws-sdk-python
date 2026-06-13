"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateMessageTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_data


class UpdateMessageTemplateResponse(TypedDict):
    message_template: NotRequired[
        "aws_sdk_qconnect.types.message_template_data.MessageTemplateData"
    ]
    """<p>The message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMessageTemplateResponse) -> dict:
    out: dict = {}
    if "message_template" in value:
        import aws_sdk_qconnect.types.message_template_data

        out["messageTemplate"] = (
            aws_sdk_qconnect.types.message_template_data.serialize_json(
                value["message_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMessageTemplateResponse:
    out: UpdateMessageTemplateResponse = {}  # type: ignore[typeddict-item]
    if "messageTemplate" in data:
        import aws_sdk_qconnect.types.message_template_data

        out["message_template"] = (
            aws_sdk_qconnect.types.message_template_data.deserialize_json(
                data["messageTemplate"]
            )
        )
    return out
