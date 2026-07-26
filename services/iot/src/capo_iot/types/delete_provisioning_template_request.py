"""Generated from Smithy shape ``com.amazonaws.iot#DeleteProvisioningTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.template_name


class DeleteProvisioningTemplateRequest(TypedDict, closed=True):
    template_name: "capo_iot.types.template_name.TemplateName"
    """<p>The name of the fleet provision template to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProvisioningTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProvisioningTemplateRequest:
    out: DeleteProvisioningTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
