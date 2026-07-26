"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssessmentTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.assessment_target

AssessmentTargets: TypeAlias = list[
    "capo_migrationhubstrategy.types.assessment_target.AssessmentTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentTargets) -> list:
    import capo_migrationhubstrategy.types.assessment_target

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.assessment_target.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssessmentTargets:
    import capo_migrationhubstrategy.types.assessment_target

    out: AssessmentTargets = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.assessment_target.deserialize_json(item)
        )
    return out
