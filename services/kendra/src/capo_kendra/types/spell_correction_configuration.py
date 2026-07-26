"""Generated from Smithy shape ``com.amazonaws.kendra#SpellCorrectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.boolean


class SpellCorrectionConfiguration(TypedDict, closed=True):
    include_query_spell_check_suggestions: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to suggest spell corrections for queries.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpellCorrectionConfiguration) -> dict:
    out: dict = {}
    out["IncludeQuerySpellCheckSuggestions"] = value.get(
        "include_query_spell_check_suggestions", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpellCorrectionConfiguration:
    out: SpellCorrectionConfiguration = {}  # type: ignore[typeddict-item]
    if "IncludeQuerySpellCheckSuggestions" in data:
        out["include_query_spell_check_suggestions"] = data[
            "IncludeQuerySpellCheckSuggestions"
        ]
    else:
        out["include_query_spell_check_suggestions"] = False
    return out
