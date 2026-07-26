"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AssessmentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.assessment_status

AssessmentStatusList: TypeAlias = list[
    "capo_resiliencehub.types.assessment_status.AssessmentStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentStatusList) -> list:
    import capo_resiliencehub.types.assessment_status

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.assessment_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssessmentStatusList:
    import capo_resiliencehub.types.assessment_status

    out: AssessmentStatusList = []
    for item in data:
        out.append(capo_resiliencehub.types.assessment_status.deserialize_json(item))
    return out
