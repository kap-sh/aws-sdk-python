"""Generated from Smithy shape ``com.amazonaws.iot#DeleteProvisioningTemplateVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.template_name
    import capo_iot.types.template_version_id


class DeleteProvisioningTemplateVersionRequest(TypedDict, closed=True):
    template_name: "capo_iot.types.template_name.TemplateName"
    """<p>The name of the provisioning template version to delete.</p>"""
    version_id: "capo_iot.types.template_version_id.TemplateVersionId"
    """<p>The provisioning template version ID to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProvisioningTemplateVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProvisioningTemplateVersionRequest:
    out: DeleteProvisioningTemplateVersionRequest = {}  # type: ignore[typeddict-item]
    return out
