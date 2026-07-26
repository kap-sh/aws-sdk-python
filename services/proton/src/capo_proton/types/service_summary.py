"""Generated from Smithy shape ``com.amazonaws.proton#ServiceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.description
    import capo_proton.types.resource_name
    import capo_proton.types.service_arn
    import capo_proton.types.service_status
    import capo_proton.types.status_message


class ServiceSummary(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the service.</p>"""
    arn: "capo_proton.types.service_arn.ServiceArn"
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the service was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The time when the service was last modified.</p>"""
    status: "capo_proton.types.service_status.ServiceStatus"
    """<p>The status of the service.</p>"""
    status_message: NotRequired["capo_proton.types.status_message.StatusMessage"]
    """<p>A service status message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["arn"] = value["arn"]
    out["templateName"] = value["template_name"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastModifiedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["last_modified_at"]
    )
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceSummary:
    out: ServiceSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ServiceSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ServiceSummary.arn required")
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("ServiceSummary.template_name required")
    if "createdAt" in data:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ServiceSummary.created_at required")
    if "lastModifiedAt" in data:
        import capo_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError("ServiceSummary.last_modified_at required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ServiceSummary.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
