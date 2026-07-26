"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#GetCloudFormationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string


class GetCloudFormationTemplateRequest(TypedDict, closed=True):
    application_id: "capo_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    template_id: "capo_serverlessapplicationrepository.types.__string.__string"
    r"""<p>The UUID returned by CreateCloudFormationTemplate.</p><p>Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCloudFormationTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCloudFormationTemplateRequest:
    out: GetCloudFormationTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
