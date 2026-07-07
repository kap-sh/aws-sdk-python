"""Generated from Smithy shape ``com.amazonaws.datazone#DetailedGlossaryTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glossary_term_name
    import aws_sdk_datazone.types.short_description


class DetailedGlossaryTerm(TypedDict, closed=True):
    name: NotRequired["aws_sdk_datazone.types.glossary_term_name.GlossaryTermName"]
    """<p>The name of a glossary term attached to the inventory asset.</p>"""
    short_description: NotRequired[
        "aws_sdk_datazone.types.short_description.ShortDescription"
    ]
    """<p>The shoft description of a glossary term attached to the inventory asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetailedGlossaryTerm) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "short_description" in value:
        out["shortDescription"] = value["short_description"]
    return out


def deserialize_json(data: dict) -> DetailedGlossaryTerm:
    out: DetailedGlossaryTerm = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "shortDescription" in data:
        out["short_description"] = data["shortDescription"]
    return out
