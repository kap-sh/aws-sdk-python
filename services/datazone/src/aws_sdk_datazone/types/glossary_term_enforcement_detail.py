"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryTermEnforcementDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glossary_term_identifiers


class GlossaryTermEnforcementDetail(TypedDict, closed=True):
    required_glossary_term_ids: NotRequired[
        "aws_sdk_datazone.types.glossary_term_identifiers.GlossaryTermIdentifiers"
    ]
    """<p>The ID of the required glossary term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryTermEnforcementDetail) -> dict:
    out: dict = {}
    if "required_glossary_term_ids" in value:
        import aws_sdk_datazone.types.glossary_term_identifiers

        out["requiredGlossaryTermIds"] = (
            aws_sdk_datazone.types.glossary_term_identifiers.serialize_json(
                value["required_glossary_term_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlossaryTermEnforcementDetail:
    out: GlossaryTermEnforcementDetail = {}  # type: ignore[typeddict-item]
    if "requiredGlossaryTermIds" in data:
        import aws_sdk_datazone.types.glossary_term_identifiers

        out["required_glossary_term_ids"] = (
            aws_sdk_datazone.types.glossary_term_identifiers.deserialize_json(
                data["requiredGlossaryTermIds"]
            )
        )
    return out
