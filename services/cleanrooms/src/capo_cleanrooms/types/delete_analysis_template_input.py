"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteAnalysisTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_identifier
    import capo_cleanrooms.types.membership_identifier


class DeleteAnalysisTemplateInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a membership resource.</p>"""
    analysis_template_identifier: (
        "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier"
    )
    """<p>The identifier for the analysis template resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAnalysisTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAnalysisTemplateInput:
    out: DeleteAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
    return out
