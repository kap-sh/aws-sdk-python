"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_description
    import aws_sdk_datazone.types.glossary_id
    import aws_sdk_datazone.types.glossary_item_additional_attributes
    import aws_sdk_datazone.types.glossary_name
    import aws_sdk_datazone.types.glossary_status
    import aws_sdk_datazone.types.glossary_usage_restrictions
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class GlossaryItem(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the business glossary exists.</p>"""
    id: "aws_sdk_datazone.types.glossary_id.GlossaryId"
    """<p>The identifier of the glossary.</p>"""
    name: "aws_sdk_datazone.types.glossary_name.GlossaryName"
    """<p>The name of the glossary.</p>"""
    owning_project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the business glosary.</p>"""
    description: NotRequired[
        "aws_sdk_datazone.types.glossary_description.GlossaryDescription"
    ]
    """<p>The business glossary description.</p>"""
    status: "aws_sdk_datazone.types.glossary_status.GlossaryStatus"
    """<p>The business glossary status.</p>"""
    usage_restrictions: NotRequired[
        "aws_sdk_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
    ]
    """<p>The usage restrictions associated with a goverened glossary term.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the glossary was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the glossary.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the business glossary was updated.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the business glossary.</p>"""
    additional_attributes: NotRequired[
        "aws_sdk_datazone.types.glossary_item_additional_attributes.GlossaryItemAdditionalAttributes"
    ]
    """<p>The additional attributes of an Amazon DataZone glossary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryItem) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["owningProjectId"] = value["owning_project_id"]
    if "description" in value:
        out["description"] = value["description"]
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
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_datazone.types.updated_at

        out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "additional_attributes" in value:
        import aws_sdk_datazone.types.glossary_item_additional_attributes

        out["additionalAttributes"] = (
            aws_sdk_datazone.types.glossary_item_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlossaryItem:
    out: GlossaryItem = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GlossaryItem.domain_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GlossaryItem.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GlossaryItem.name required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("GlossaryItem.owning_project_id required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_datazone.types.glossary_status

        out["status"] = aws_sdk_datazone.types.glossary_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GlossaryItem.status required")
    if "usageRestrictions" in data:
        import aws_sdk_datazone.types.glossary_usage_restrictions

        out["usage_restrictions"] = (
            aws_sdk_datazone.types.glossary_usage_restrictions.deserialize_json(
                data["usageRestrictions"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "additionalAttributes" in data:
        import aws_sdk_datazone.types.glossary_item_additional_attributes

        out["additional_attributes"] = (
            aws_sdk_datazone.types.glossary_item_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    return out
