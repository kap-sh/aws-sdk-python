"""Generated from Smithy shape ``com.amazonaws.resiliencehub#StartAppAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_assessment


class StartAppAssessmentResponse(TypedDict, closed=True):
    assessment: "capo_resiliencehub.types.app_assessment.AppAssessment"
    """<p>The assessment created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAppAssessmentResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.app_assessment

    out["assessment"] = capo_resiliencehub.types.app_assessment.serialize_json(
        value["assessment"]
    )
    return out


def deserialize_json(data: dict) -> StartAppAssessmentResponse:
    out: StartAppAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "assessment" in data:
        import capo_resiliencehub.types.app_assessment

        out["assessment"] = capo_resiliencehub.types.app_assessment.deserialize_json(
            data["assessment"]
        )
    else:
        raise DeserializationError("StartAppAssessmentResponse.assessment required")
    return out
