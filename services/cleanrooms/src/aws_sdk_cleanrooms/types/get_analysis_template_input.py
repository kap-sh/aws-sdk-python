"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetAnalysisTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_identifier
    import aws_sdk_cleanrooms.types.membership_identifier


class GetAnalysisTemplateInput(TypedDict, closed=True):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a membership resource.</p>"""
    analysis_template_identifier: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier"
    """<p>The identifier for the analysis template resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnalysisTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAnalysisTemplateInput:
    out: GetAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
    return out
