"""Generated from Smithy shape ``com.amazonaws.datazone#TermRelations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.glossary_terms


class TermRelations(TypedDict, closed=True):
    is_a: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The <code>isA</code> property of the term relations.</p>"""
    classifies: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The classifies of the term relations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TermRelations) -> dict:
    out: dict = {}
    if "is_a" in value:
        import capo_datazone.types.glossary_terms

        out["isA"] = capo_datazone.types.glossary_terms.serialize_json(value["is_a"])
    if "classifies" in value:
        import capo_datazone.types.glossary_terms

        out["classifies"] = capo_datazone.types.glossary_terms.serialize_json(
            value["classifies"]
        )
    return out


def deserialize_json(data: dict) -> TermRelations:
    out: TermRelations = {}  # type: ignore[typeddict-item]
    if "isA" in data:
        import capo_datazone.types.glossary_terms

        out["is_a"] = capo_datazone.types.glossary_terms.deserialize_json(data["isA"])
    if "classifies" in data:
        import capo_datazone.types.glossary_terms

        out["classifies"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["classifies"]
        )
    return out
