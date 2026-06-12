"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetInAppTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.in_app_template_response


class GetInAppTemplateResponse(TypedDict):
    in_app_template_response: NotRequired[
        "aws_sdk_pinpoint.types.in_app_template_response.InAppTemplateResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetInAppTemplateResponse) -> dict:
    out: dict = {}
    if "in_app_template_response" in value:
        import aws_sdk_pinpoint.types.in_app_template_response

        out["InAppTemplateResponse"] = (
            aws_sdk_pinpoint.types.in_app_template_response.serialize_json(
                value["in_app_template_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetInAppTemplateResponse:
    out: GetInAppTemplateResponse = {}  # type: ignore[typeddict-item]
    if "InAppTemplateResponse" in data:
        import aws_sdk_pinpoint.types.in_app_template_response

        out["in_app_template_response"] = (
            aws_sdk_pinpoint.types.in_app_template_response.deserialize_json(
                data["InAppTemplateResponse"]
            )
        )
    return out
