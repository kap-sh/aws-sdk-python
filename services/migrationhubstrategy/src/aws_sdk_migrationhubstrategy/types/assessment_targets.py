"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssessmentTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.assessment_target

AssessmentTargets: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.assessment_target.AssessmentTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentTargets) -> list:
    import aws_sdk_migrationhubstrategy.types.assessment_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.assessment_target.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssessmentTargets:
    import aws_sdk_migrationhubstrategy.types.assessment_target

    out: AssessmentTargets = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.assessment_target.deserialize_json(item)
        )
    return out
