"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateGlossaryTermOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_id
    import aws_sdk_datazone.types.glossary_term_id
    import aws_sdk_datazone.types.glossary_term_name
    import aws_sdk_datazone.types.glossary_term_status
    import aws_sdk_datazone.types.glossary_usage_restrictions
    import aws_sdk_datazone.types.long_description
    import aws_sdk_datazone.types.short_description
    import aws_sdk_datazone.types.term_relations


class UpdateGlossaryTermOutput(TypedDict):
    id: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The identifier of the business glossary term that is to be updated.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a business glossary term is to be updated.</p>"""
    glossary_id: "aws_sdk_datazone.types.glossary_id.GlossaryId"
    """<p>The identifier of the business glossary in which a term is to be updated.</p>"""
    name: "aws_sdk_datazone.types.glossary_term_name.GlossaryTermName"
    """<p>The name to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""
    status: "aws_sdk_datazone.types.glossary_term_status.GlossaryTermStatus"
    """<p>The status to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""
    short_description: NotRequired[
        "aws_sdk_datazone.types.short_description.ShortDescription"
    ]
    """<p>The short description to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""
    long_description: NotRequired[
        "aws_sdk_datazone.types.long_description.LongDescription"
    ]
    """<p>The long description to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""
    term_relations: NotRequired["aws_sdk_datazone.types.term_relations.TermRelations"]
    """<p>The term relations to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""
    usage_restrictions: NotRequired[
        "aws_sdk_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
    ]
    """<p>The usage restriction of a term within a restricted glossary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlossaryTermOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["glossaryId"] = value["glossary_id"]
    out["name"] = value["name"]
    import aws_sdk_datazone.types.glossary_term_status

    out["status"] = aws_sdk_datazone.types.glossary_term_status.serialize_json(
        value["status"]
    )
    if "short_description" in value:
        out["shortDescription"] = value["short_description"]
    if "long_description" in value:
        out["longDescription"] = value["long_description"]
    if "term_relations" in value:
        import aws_sdk_datazone.types.term_relations

        out["termRelations"] = aws_sdk_datazone.types.term_relations.serialize_json(
            value["term_relations"]
        )
    if "usage_restrictions" in value:
        import aws_sdk_datazone.types.glossary_usage_restrictions

        out["usageRestrictions"] = (
            aws_sdk_datazone.types.glossary_usage_restrictions.serialize_json(
                value["usage_restrictions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGlossaryTermOutput:
    out: UpdateGlossaryTermOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateGlossaryTermOutput.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("UpdateGlossaryTermOutput.domain_id required")
    if "glossaryId" in data:
        out["glossary_id"] = data["glossaryId"]
    else:
        raise DeserializationError("UpdateGlossaryTermOutput.glossary_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateGlossaryTermOutput.name required")
    if "status" in data:
        import aws_sdk_datazone.types.glossary_term_status

        out["status"] = aws_sdk_datazone.types.glossary_term_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateGlossaryTermOutput.status required")
    if "shortDescription" in data:
        out["short_description"] = data["shortDescription"]
    if "longDescription" in data:
        out["long_description"] = data["longDescription"]
    if "termRelations" in data:
        import aws_sdk_datazone.types.term_relations

        out["term_relations"] = aws_sdk_datazone.types.term_relations.deserialize_json(
            data["termRelations"]
        )
    if "usageRestrictions" in data:
        import aws_sdk_datazone.types.glossary_usage_restrictions

        out["usage_restrictions"] = (
            aws_sdk_datazone.types.glossary_usage_restrictions.deserialize_json(
                data["usageRestrictions"]
            )
        )
    return out
