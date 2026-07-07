"""Generated from Smithy shape ``com.amazonaws.datazone#AssociateGovernedTermsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_identifier
    import aws_sdk_datazone.types.governed_entity_type
    import aws_sdk_datazone.types.governed_glossary_terms


class AssociateGovernedTermsInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where governed terms are to be associated with an asset.</p>"""
    entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the asset with which you want to associate a governed term.</p>"""
    entity_type: "aws_sdk_datazone.types.governed_entity_type.GovernedEntityType"
    """<p>The type of the asset with which you want to associate a governed term.</p>"""
    governed_glossary_terms: (
        "aws_sdk_datazone.types.governed_glossary_terms.GovernedGlossaryTerms"
    )
    """<p>The glossary terms in a restricted glossary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateGovernedTermsInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.governed_glossary_terms

    out["governedGlossaryTerms"] = (
        aws_sdk_datazone.types.governed_glossary_terms.serialize_json(
            value["governed_glossary_terms"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssociateGovernedTermsInput:
    out: AssociateGovernedTermsInput = {}  # type: ignore[typeddict-item]
    if "governedGlossaryTerms" in data:
        import aws_sdk_datazone.types.governed_glossary_terms

        out["governed_glossary_terms"] = (
            aws_sdk_datazone.types.governed_glossary_terms.deserialize_json(
                data["governedGlossaryTerms"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateGovernedTermsInput.governed_glossary_terms required"
        )
    return out
