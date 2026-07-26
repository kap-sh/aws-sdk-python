"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetSmsTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.sms_template_response


class GetSmsTemplateResponse(TypedDict, closed=True):
    sms_template_response: NotRequired[
        "capo_pinpoint.types.sms_template_response.SMSTemplateResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetSmsTemplateResponse) -> dict:
    out: dict = {}
    if "sms_template_response" in value:
        import capo_pinpoint.types.sms_template_response

        out["SMSTemplateResponse"] = (
            capo_pinpoint.types.sms_template_response.serialize_json(
                value["sms_template_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSmsTemplateResponse:
    out: GetSmsTemplateResponse = {}  # type: ignore[typeddict-item]
    if "SMSTemplateResponse" in data:
        import capo_pinpoint.types.sms_template_response

        out["sms_template_response"] = (
            capo_pinpoint.types.sms_template_response.deserialize_json(
                data["SMSTemplateResponse"]
            )
        )
    return out
