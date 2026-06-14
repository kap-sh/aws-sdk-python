"""Generated from Smithy shape ``com.amazonaws.datazone#CreateGlossaryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_description
    import aws_sdk_datazone.types.glossary_name
    import aws_sdk_datazone.types.glossary_status
    import aws_sdk_datazone.types.glossary_usage_restrictions
    import aws_sdk_datazone.types.project_id


class CreateGlossaryInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this business glossary is created.</p>"""
    name: "aws_sdk_datazone.types.glossary_name.GlossaryName"
    """<p>The name of this business glossary.</p>"""
    owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the project that currently owns business glossary.</p>"""
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
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGlossaryInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateGlossaryInput:
    out: CreateGlossaryInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateGlossaryInput.name required")
    if "owningProjectIdentifier" in data:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "CreateGlossaryInput.owning_project_identifier required"
        )
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
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
