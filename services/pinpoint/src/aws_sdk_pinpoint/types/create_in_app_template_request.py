"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateInAppTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.in_app_template_request


class CreateInAppTemplateRequest(TypedDict):
    in_app_template_request: NotRequired[
        "aws_sdk_pinpoint.types.in_app_template_request.InAppTemplateRequest"
    ]
    template_name: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInAppTemplateRequest) -> dict:
    out: dict = {}
    if "in_app_template_request" in value:
        import aws_sdk_pinpoint.types.in_app_template_request

        out["InAppTemplateRequest"] = (
            aws_sdk_pinpoint.types.in_app_template_request.serialize_json(
                value["in_app_template_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateInAppTemplateRequest:
    out: CreateInAppTemplateRequest = {}  # type: ignore[typeddict-item]
    if "InAppTemplateRequest" in data:
        import aws_sdk_pinpoint.types.in_app_template_request

        out["in_app_template_request"] = (
            aws_sdk_pinpoint.types.in_app_template_request.deserialize_json(
                data["InAppTemplateRequest"]
            )
        )
    return out
