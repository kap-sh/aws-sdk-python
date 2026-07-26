"""Generated from Smithy shape ``com.amazonaws.proton#ServiceTemplateVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.description
    import capo_proton.types.resource_name
    import capo_proton.types.service_template_version_arn
    import capo_proton.types.status_message
    import capo_proton.types.template_version_part
    import capo_proton.types.template_version_status


class ServiceTemplateVersionSummary(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    major_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>The latest major version that's associated with the version of a service template.</p>"""
    minor_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>The minor version of a service template.</p>"""
    recommended_minor_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The recommended minor version of the service template.</p>"""
    status: "capo_proton.types.template_version_status.TemplateVersionStatus"
    """<p>The service template minor version status.</p>"""
    status_message: NotRequired["capo_proton.types.status_message.StatusMessage"]
    """<p>A service template minor version status message.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the version of a service template.</p>"""
    arn: "capo_proton.types.service_template_version_arn.ServiceTemplateVersionArn"
    """<p>The Amazon Resource Name (ARN) of the version of a service template.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the version of a service template was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The time when the version of a service template was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceTemplateVersionSummary) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    if "recommended_minor_version" in value:
        out["recommendedMinorVersion"] = value["recommended_minor_version"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "description" in value:
        out["description"] = value["description"]
    out["arn"] = value["arn"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastModifiedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["last_modified_at"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceTemplateVersionSummary:
    out: ServiceTemplateVersionSummary = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "ServiceTemplateVersionSummary.template_name required"
        )
    if "majorVersion" in data:
        out["major_version"] = data["majorVersion"]
    else:
        raise DeserializationError(
            "ServiceTemplateVersionSummary.major_version required"
        )
    if "minorVersion" in data:
        out["minor_version"] = data["minorVersion"]
    else:
        raise DeserializationError(
            "ServiceTemplateVersionSummary.minor_version required"
        )
    if "recommendedMinorVersion" in data:
        out["recommended_minor_version"] = data["recommendedMinorVersion"]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ServiceTemplateVersionSummary.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "description" in data:
        out["description"] = data["description"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ServiceTemplateVersionSummary.arn required")
    if "createdAt" in data:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ServiceTemplateVersionSummary.created_at required")
    if "lastModifiedAt" in data:
        import capo_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceTemplateVersionSummary.last_modified_at required"
        )
    return out
