"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssessmentTargetValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.string

AssessmentTargetValues: TypeAlias = list[
    "capo_migrationhubstrategy.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentTargetValues) -> list:
    return list(value)


def deserialize_json(data: list) -> AssessmentTargetValues:
    return list(data)
