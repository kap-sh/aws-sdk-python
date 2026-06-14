"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateGlossaryTermInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_term_id
    import aws_sdk_datazone.types.glossary_term_name
    import aws_sdk_datazone.types.glossary_term_status
    import aws_sdk_datazone.types.long_description
    import aws_sdk_datazone.types.short_description
    import aws_sdk_datazone.types.term_relations


class UpdateGlossaryTermInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a business glossary term is to be updated.</p>"""
    glossary_identifier: NotRequired[
        "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
    ]
    """<p>The identifier of the business glossary in which a term is to be updated.</p>"""
    identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The identifier of the business glossary term that is to be updated.</p>"""
    name: NotRequired["aws_sdk_datazone.types.glossary_term_name.GlossaryTermName"]
    """<p>The name to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""
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
    status: NotRequired[
        "aws_sdk_datazone.types.glossary_term_status.GlossaryTermStatus"
    ]
    """<p>The status to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlossaryTermInput) -> dict:
    out: dict = {}
    if "glossary_identifier" in value:
        out["glossaryIdentifier"] = value["glossary_identifier"]
    if "name" in value:
        out["name"] = value["name"]
    if "short_description" in value:
        out["shortDescription"] = value["short_description"]
    if "long_description" in value:
        out["longDescription"] = value["long_description"]
    if "term_relations" in value:
        import aws_sdk_datazone.types.term_relations

        out["termRelations"] = aws_sdk_datazone.types.term_relations.serialize_json(
            value["term_relations"]
        )
    if "status" in value:
        import aws_sdk_datazone.types.glossary_term_status

        out["status"] = aws_sdk_datazone.types.glossary_term_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateGlossaryTermInput:
    out: UpdateGlossaryTermInput = {}  # type: ignore[typeddict-item]
    if "glossaryIdentifier" in data:
        out["glossary_identifier"] = data["glossaryIdentifier"]
    if "name" in data:
        out["name"] = data["name"]
    if "shortDescription" in data:
        out["short_description"] = data["shortDescription"]
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
    return out
