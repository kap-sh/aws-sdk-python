"""Generated from Smithy shape ``com.amazonaws.datazone#DisassociateGovernedTermsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_identifier
    import aws_sdk_datazone.types.governed_entity_type
    import aws_sdk_datazone.types.governed_glossary_terms


class DisassociateGovernedTermsInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to disassociate restricted terms from an asset.</p>"""
    entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of an asset from which you want to disassociate restricted terms.</p>"""
    entity_type: "aws_sdk_datazone.types.governed_entity_type.GovernedEntityType"
    """<p>The type of the asset from which you want to disassociate restricted terms.</p>"""
    governed_glossary_terms: (
        "aws_sdk_datazone.types.governed_glossary_terms.GovernedGlossaryTerms"
    )
    """<p>The restricted glossary terms that you want to disassociate from an asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateGovernedTermsInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.governed_glossary_terms

    out["governedGlossaryTerms"] = (
        aws_sdk_datazone.types.governed_glossary_terms.serialize_json(
            value["governed_glossary_terms"]
        )
    )
    return out


def deserialize_json(data: dict) -> DisassociateGovernedTermsInput:
    out: DisassociateGovernedTermsInput = {}  # type: ignore[typeddict-item]
    if "governedGlossaryTerms" in data:
        import aws_sdk_datazone.types.governed_glossary_terms

        out["governed_glossary_terms"] = (
            aws_sdk_datazone.types.governed_glossary_terms.deserialize_json(
                data["governedGlossaryTerms"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateGovernedTermsInput.governed_glossary_terms required"
        )
    return out
