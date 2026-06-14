"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateGlossaryOutput``."""

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


class UpdateGlossaryOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a business glossary is to be updated.</p>"""
    id: "aws_sdk_datazone.types.glossary_id.GlossaryId"
    """<p>The identifier of the business glossary that is to be updated.</p>"""
    name: "aws_sdk_datazone.types.glossary_name.GlossaryName"
    """<p>The name to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    owning_project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project in which to update a business glossary.</p>"""
    description: NotRequired[
        "aws_sdk_datazone.types.glossary_description.GlossaryDescription"
    ]
    """<p>The description to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    status: NotRequired["aws_sdk_datazone.types.glossary_status.GlossaryStatus"]
    """<p>The status to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    usage_restrictions: NotRequired[
        "aws_sdk_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
    ]
    """<p>The usage restriction of the restricted glossary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlossaryOutput) -> dict:
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


def deserialize_json(data: dict) -> UpdateGlossaryOutput:
    out: UpdateGlossaryOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("UpdateGlossaryOutput.domain_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateGlossaryOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateGlossaryOutput.name required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("UpdateGlossaryOutput.owning_project_id required")
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
