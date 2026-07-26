"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateSmsTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.sms_template_request


class CreateSmsTemplateRequest(TypedDict, closed=True):
    sms_template_request: NotRequired[
        "capo_pinpoint.types.sms_template_request.SMSTemplateRequest"
    ]
    template_name: "capo_pinpoint.types.__string.__string"
    """<p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSmsTemplateRequest) -> dict:
    out: dict = {}
    if "sms_template_request" in value:
        import capo_pinpoint.types.sms_template_request

        out["SMSTemplateRequest"] = (
            capo_pinpoint.types.sms_template_request.serialize_json(
                value["sms_template_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSmsTemplateRequest:
    out: CreateSmsTemplateRequest = {}  # type: ignore[typeddict-item]
    if "SMSTemplateRequest" in data:
        import capo_pinpoint.types.sms_template_request

        out["sms_template_request"] = (
            capo_pinpoint.types.sms_template_request.deserialize_json(
                data["SMSTemplateRequest"]
            )
        )
    return out
