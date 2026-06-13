"""Generated from Smithy shape ``com.amazonaws.datazone#CreateGlossaryOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_description
    import aws_sdk_datazone.types.glossary_id
    import aws_sdk_datazone.types.glossary_name
    import aws_sdk_datazone.types.glossary_status
    import aws_sdk_datazone.types.glossary_usage_restrictions
    import aws_sdk_datazone.types.project_id


class CreateGlossaryOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this business glossary is created.</p>"""
    id: "aws_sdk_datazone.types.glossary_id.GlossaryId"
    """<p>The ID of this business glossary.</p>"""
    name: "aws_sdk_datazone.types.glossary_name.GlossaryName"
    """<p>The name of this business glossary.</p>"""
    owning_project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the project that currently owns this business glossary.</p>"""
    description: NotRequired[
        "aws_sdk_datazone.types.glossary_description.GlossaryDescription"
    ]
    """<p>The description of this business glossary.</p>"""
    status: NotRequired["aws_sdk_datazone.types.glossary_status.GlossaryStatus"]
    """<p>The status of this business glossary.</p>"""
    usage_restrictions: NotRequired[
        "aws_sdk_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
    ]
    """<p>The usage restriction of the restricted glossary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGlossaryOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["owningProjectId"] = value["owning_project_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_datazone.types.glossary_status

        out["status"] = aws_sdk_datazone.types.glossary_status.serialize_json(
            value["status"]
        )
    if "usage_restrictions" in value:
        import aws_sdk_datazone.types.glossary_usage_restrictions

        out["usageRestrictions"] = (
            aws_sdk_datazone.types.glossary_usage_restrictions.serialize_json(
                value["usage_restrictions"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGlossaryOutput:
    out: CreateGlossaryOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateGlossaryOutput.domain_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateGlossaryOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateGlossaryOutput.name required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("CreateGlossaryOutput.owning_project_id required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_datazone.types.glossary_status

        out["status"] = aws_sdk_datazone.types.glossary_status.deserialize_json(
            data["status"]
        )
    if "usageRestrictions" in data:
        import aws_sdk_datazone.types.glossary_usage_restrictions

        out["usage_restrictions"] = (
            aws_sdk_datazone.types.glossary_usage_restrictions.deserialize_json(
                data["usageRestrictions"]
            )
        )
    return out
