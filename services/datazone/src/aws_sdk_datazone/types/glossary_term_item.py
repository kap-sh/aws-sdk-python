"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryTermItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_id
    import aws_sdk_datazone.types.glossary_term_id
    import aws_sdk_datazone.types.glossary_term_item_additional_attributes
    import aws_sdk_datazone.types.glossary_term_name
    import aws_sdk_datazone.types.glossary_term_status
    import aws_sdk_datazone.types.glossary_usage_restrictions
    import aws_sdk_datazone.types.long_description
    import aws_sdk_datazone.types.short_description
    import aws_sdk_datazone.types.term_relations
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class GlossaryTermItem(TypedDict, closed=True):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the business glossary exists.</p>"""
    glossary_id: "aws_sdk_datazone.types.glossary_id.GlossaryId"
    """<p>The identifier of the business glossary to which the term belongs.</p>"""
    id: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The identifier of the business glossary term.</p>"""
    name: "aws_sdk_datazone.types.glossary_term_name.GlossaryTermName"
    """<p>The name of the business glossary term.</p>"""
    short_description: NotRequired[
        "aws_sdk_datazone.types.short_description.ShortDescription"
    ]
    """<p>The short description of the business glossary term.</p>"""
    usage_restrictions: NotRequired[
        "aws_sdk_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
    ]
    """<p>The usage restrictions associated with a goverened glossary term.</p>"""
    long_description: NotRequired[
        "aws_sdk_datazone.types.long_description.LongDescription"
    ]
    """<p>The long description of the business glossary term.</p>"""
    term_relations: NotRequired["aws_sdk_datazone.types.term_relations.TermRelations"]
    """<p>The relations of the business glossary term.</p>"""
    status: "aws_sdk_datazone.types.glossary_term_status.GlossaryTermStatus"
    """<p>The status of the business glossary term.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when a business glossary term was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the business glossary.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when a business glossary term was updated.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the business glossary term.</p>"""
    additional_attributes: NotRequired[
        "aws_sdk_datazone.types.glossary_term_item_additional_attributes.GlossaryTermItemAdditionalAttributes"
    ]
    """<p>The additional attributes of an Amazon DataZone glossary term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryTermItem) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["glossaryId"] = value["glossary_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "short_description" in value:
        out["shortDescription"] = value["short_description"]
    if "usage_restrictions" in value:
        import aws_sdk_datazone.types.glossary_usage_restrictions

        out["usageRestrictions"] = (
            aws_sdk_datazone.types.glossary_usage_restrictions.serialize_json(
                value["usage_restrictions"]
            )
        )
    if "long_description" in value:
        out["longDescription"] = value["long_description"]
    if "term_relations" in value:
        import aws_sdk_datazone.types.term_relations

        out["termRelations"] = aws_sdk_datazone.types.term_relations.serialize_json(
            value["term_relations"]
        )
    import aws_sdk_datazone.types.glossary_term_status

    out["status"] = aws_sdk_datazone.types.glossary_term_status.serialize_json(
        value["status"]
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
        import aws_sdk_datazone.types.glossary_term_item_additional_attributes

        out["additionalAttributes"] = (
            aws_sdk_datazone.types.glossary_term_item_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlossaryTermItem:
    out: GlossaryTermItem = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GlossaryTermItem.domain_id required")
    if "glossaryId" in data:
        out["glossary_id"] = data["glossaryId"]
    else:
        raise DeserializationError("GlossaryTermItem.glossary_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GlossaryTermItem.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GlossaryTermItem.name required")
    if "shortDescription" in data:
        out["short_description"] = data["shortDescription"]
    if "usageRestrictions" in data:
        import aws_sdk_datazone.types.glossary_usage_restrictions

        out["usage_restrictions"] = (
            aws_sdk_datazone.types.glossary_usage_restrictions.deserialize_json(
                data["usageRestrictions"]
            )
        )
    if "longDescription" in data:
        out["long_description"] = data["longDescription"]
    if "termRelations" in data:
        import aws_sdk_datazone.types.term_relations

        out["term_relations"] = aws_sdk_datazone.types.term_relations.deserialize_json(
            data["termRelations"]
        )
    if "status" in data:
        import aws_sdk_datazone.types.glossary_term_status

        out["status"] = aws_sdk_datazone.types.glossary_term_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GlossaryTermItem.status required")
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
        import aws_sdk_datazone.types.glossary_term_item_additional_attributes

        out["additional_attributes"] = (
            aws_sdk_datazone.types.glossary_term_item_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    return out
