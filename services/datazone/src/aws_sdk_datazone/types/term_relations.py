"""Generated from Smithy shape ``com.amazonaws.datazone#TermRelations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glossary_terms


class TermRelations(TypedDict):
    is_a: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The <code>isA</code> property of the term relations.</p>"""
    classifies: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The classifies of the term relations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TermRelations) -> dict:
    out: dict = {}
    if "is_a" in value:
        import aws_sdk_datazone.types.glossary_terms

        out["isA"] = aws_sdk_datazone.types.glossary_terms.serialize_json(value["is_a"])
    if "classifies" in value:
        import aws_sdk_datazone.types.glossary_terms

        out["classifies"] = aws_sdk_datazone.types.glossary_terms.serialize_json(
            value["classifies"]
        )
    return out


def deserialize_json(data: dict) -> TermRelations:
    out: TermRelations = {}  # type: ignore[typeddict-item]
    if "isA" in data:
        import aws_sdk_datazone.types.glossary_terms

        out["is_a"] = aws_sdk_datazone.types.glossary_terms.deserialize_json(
            data["isA"]
        )
    if "classifies" in data:
        import aws_sdk_datazone.types.glossary_terms

        out["classifies"] = aws_sdk_datazone.types.glossary_terms.deserialize_json(
            data["classifies"]
        )
    return out
