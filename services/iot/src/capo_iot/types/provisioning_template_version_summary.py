"""Generated from Smithy shape ``com.amazonaws.iot#ProvisioningTemplateVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.date_type
    import capo_iot.types.is_default_version
    import capo_iot.types.template_version_id


class ProvisioningTemplateVersionSummary(TypedDict, closed=True):
    version_id: NotRequired["capo_iot.types.template_version_id.TemplateVersionId"]
    """<p>The ID of the fleet provisioning template version.</p>"""
    creation_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date when the provisioning template version was created</p>"""
    is_default_version: "capo_iot.types.is_default_version.IsDefaultVersion"
    """<p>True if the provisioning template version is the default version, otherwise false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningTemplateVersionSummary) -> dict:
    out: dict = {}
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    if "creation_date" in value:
        import capo_iot.types.date_type

        out["creationDate"] = capo_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    out["isDefaultVersion"] = value.get("is_default_version", False)
    return out


def deserialize_json(data: dict) -> ProvisioningTemplateVersionSummary:
    out: ProvisioningTemplateVersionSummary = {}  # type: ignore[typeddict-item]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    if "creationDate" in data:
        import capo_iot.types.date_type

        out["creation_date"] = capo_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    if "isDefaultVersion" in data:
        out["is_default_version"] = data["isDefaultVersion"]
    else:
        out["is_default_version"] = False
    return out
