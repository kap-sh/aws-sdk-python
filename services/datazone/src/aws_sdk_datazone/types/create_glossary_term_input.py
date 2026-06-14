"""Generated from Smithy shape ``com.amazonaws.datazone#CreateGlossaryTermInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_term_id
    import aws_sdk_datazone.types.glossary_term_name
    import aws_sdk_datazone.types.glossary_term_status
    import aws_sdk_datazone.types.long_description
    import aws_sdk_datazone.types.short_description
    import aws_sdk_datazone.types.term_relations


class CreateGlossaryTermInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this business glossary term is created.</p>"""
    glossary_identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
    """<p>The ID of the business glossary in which this term is created.</p>"""
    name: "aws_sdk_datazone.types.glossary_term_name.GlossaryTermName"
    """<p>The name of this business glossary term.</p>"""
    status: NotRequired[
        "aws_sdk_datazone.types.glossary_term_status.GlossaryTermStatus"
    ]
    """<p>The status of this business glossary term.</p>"""
    short_description: NotRequired[
        "aws_sdk_datazone.types.short_description.ShortDescription"
    ]
    """<p>The short description of this business glossary term.</p>"""
    long_description: NotRequired[
        "aws_sdk_datazone.types.long_description.LongDescription"
    ]
    """<p>The long description of this business glossary term.</p>"""
    term_relations: NotRequired["aws_sdk_datazone.types.term_relations.TermRelations"]
    """<p>The term relations of this business glossary term.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGlossaryTermInput) -> dict:
    out: dict = {}
    out["glossaryIdentifier"] = value["glossary_identifier"]
    out["name"] = value["name"]
    if "status" in value:
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateGlossaryTermInput:
    out: CreateGlossaryTermInput = {}  # type: ignore[typeddict-item]
    if "glossaryIdentifier" in data:
        out["glossary_identifier"] = data["glossaryIdentifier"]
    else:
        raise DeserializationError(
            "CreateGlossaryTermInput.glossary_identifier required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateGlossaryTermInput.name required")
    if "status" in data:
        import aws_sdk_datazone.types.glossary_term_status

        out["status"] = aws_sdk_datazone.types.glossary_term_status.deserialize_json(
            data["status"]
        )
    if "shortDescription" in data:
        out["short_description"] = data["shortDescription"]
    if "longDescription" in data:
        out["long_description"] = data["longDescription"]
    if "termRelations" in data:
        import aws_sdk_datazone.types.term_relations

        out["term_relations"] = aws_sdk_datazone.types.term_relations.deserialize_json(
            data["termRelations"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
