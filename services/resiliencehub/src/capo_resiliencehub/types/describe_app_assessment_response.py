"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeAppAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_assessment


class DescribeAppAssessmentResponse(TypedDict, closed=True):
    assessment: "capo_resiliencehub.types.app_assessment.AppAssessment"
    """<p>The assessment for an Resilience Hub application, returned as an object. This object includes Amazon Resource Names (ARNs), compliance information, compliance status, cost, messages, resiliency scores, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppAssessmentResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.app_assessment

    out["assessment"] = capo_resiliencehub.types.app_assessment.serialize_json(
        value["assessment"]
    )
    return out


def deserialize_json(data: dict) -> DescribeAppAssessmentResponse:
    out: DescribeAppAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "assessment" in data:
        import capo_resiliencehub.types.app_assessment

        out["assessment"] = capo_resiliencehub.types.app_assessment.deserialize_json(
            data["assessment"]
        )
    else:
        raise DeserializationError("DescribeAppAssessmentResponse.assessment required")
    return out
