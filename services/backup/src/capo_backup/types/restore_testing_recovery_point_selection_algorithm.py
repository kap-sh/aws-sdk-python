"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingRecoveryPointSelectionAlgorithm``."""

from typing import Literal, TypeAlias, cast

RestoreTestingRecoveryPointSelectionAlgorithm: TypeAlias = Literal[
    "LATEST_WITHIN_WINDOW",
    "RANDOM_WITHIN_WINDOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingRecoveryPointSelectionAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> RestoreTestingRecoveryPointSelectionAlgorithm:
    return cast(RestoreTestingRecoveryPointSelectionAlgorithm, data)
