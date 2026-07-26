"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetEmailTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.email_template_response


class GetEmailTemplateResponse(TypedDict, closed=True):
    email_template_response: NotRequired[
        "capo_pinpoint.types.email_template_response.EmailTemplateResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailTemplateResponse) -> dict:
    out: dict = {}
    if "email_template_response" in value:
        import capo_pinpoint.types.email_template_response

        out["EmailTemplateResponse"] = (
            capo_pinpoint.types.email_template_response.serialize_json(
                value["email_template_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEmailTemplateResponse:
    out: GetEmailTemplateResponse = {}  # type: ignore[typeddict-item]
    if "EmailTemplateResponse" in data:
        import capo_pinpoint.types.email_template_response

        out["email_template_response"] = (
            capo_pinpoint.types.email_template_response.deserialize_json(
                data["EmailTemplateResponse"]
            )
        )
    return out
