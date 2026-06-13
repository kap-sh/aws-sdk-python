"""Generated from Smithy shape ``com.amazonaws.proton#ServiceTemplateSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.display_name
    import aws_sdk_proton.types.full_template_version_number
    import aws_sdk_proton.types.provisioning
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.service_template_arn


class ServiceTemplateSummary(TypedDict):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    arn: "aws_sdk_proton.types.service_template_arn.ServiceTemplateArn"
    """<p>The Amazon Resource Name (ARN) of the service template.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the service template was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The time when the service template was last modified.</p>"""
    display_name: NotRequired["aws_sdk_proton.types.display_name.DisplayName"]
    """<p>The service template name as displayed in the developer interface.</p>"""
    description: NotRequired["aws_sdk_proton.types.description.Description"]
    """<p>A description of the service template.</p>"""
    recommended_version: NotRequired[
        "aws_sdk_proton.types.full_template_version_number.FullTemplateVersionNumber"
    ]
    """<p>The recommended version of the service template.</p>"""
    pipeline_provisioning: NotRequired["aws_sdk_proton.types.provisioning.Provisioning"]
    """<p>If <code>pipelineProvisioning</code> is <code>true</code>, a service pipeline is included in the service template, otherwise a service pipeline <i>isn't</i> included in the service template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceTemplateSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    import aws_sdk_proton.types._prelude.timestamp

    out["createdAt"] = aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import aws_sdk_proton.types._prelude.timestamp

    out["lastModifiedAt"] = (
        aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_modified_at"]
        )
    )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "recommended_version" in value:
        out["recommendedVersion"] = value["recommended_version"]
    if "pipeline_provisioning" in value:
        out["pipelineProvisioning"] = value["pipeline_provisioning"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceTemplateSummary:
    out: ServiceTemplateSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ServiceTemplateSummary.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ServiceTemplateSummary.arn required")
    if "createdAt" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ServiceTemplateSummary.created_at required")
    if "lastModifiedAt" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError("ServiceTemplateSummary.last_modified_at required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "recommendedVersion" in data:
        out["recommended_version"] = data["recommendedVersion"]
    if "pipelineProvisioning" in data:
        out["pipeline_provisioning"] = data["pipelineProvisioning"]
    return out
