"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateTemplateActiveVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.template_active_version_request


class UpdateTemplateActiveVersionRequest(TypedDict, closed=True):
    template_active_version_request: NotRequired[
        "capo_pinpoint.types.template_active_version_request.TemplateActiveVersionRequest"
    ]
    template_name: "capo_pinpoint.types.__string.__string"
    """<p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>"""
    template_type: "capo_pinpoint.types.__string.__string"
    """<p>The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplateActiveVersionRequest) -> dict:
    out: dict = {}
    if "template_active_version_request" in value:
        import capo_pinpoint.types.template_active_version_request

        out["TemplateActiveVersionRequest"] = (
            capo_pinpoint.types.template_active_version_request.serialize_json(
                value["template_active_version_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTemplateActiveVersionRequest:
    out: UpdateTemplateActiveVersionRequest = {}  # type: ignore[typeddict-item]
    if "TemplateActiveVersionRequest" in data:
        import capo_pinpoint.types.template_active_version_request

        out["template_active_version_request"] = (
            capo_pinpoint.types.template_active_version_request.deserialize_json(
                data["TemplateActiveVersionRequest"]
            )
        )
    return out
