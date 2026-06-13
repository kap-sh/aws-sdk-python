"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateAnalysisTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_identifier
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.resource_description


class UpdateAnalysisTemplateInput(TypedDict):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a membership resource.</p>"""
    analysis_template_identifier: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier"
    """<p>The identifier for the analysis template resource.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>A new description for the analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnalysisTemplateInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateAnalysisTemplateInput:
    out: UpdateAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
