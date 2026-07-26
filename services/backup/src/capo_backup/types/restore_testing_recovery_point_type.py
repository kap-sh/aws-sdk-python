"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingRecoveryPointType``."""

from typing import Literal, TypeAlias, cast

RestoreTestingRecoveryPointType: TypeAlias = Literal[
    "CONTINUOUS",
    "SNAPSHOT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingRecoveryPointType) -> str:
    return value


def deserialize_json(data: str) -> RestoreTestingRecoveryPointType:
    return cast(RestoreTestingRecoveryPointType, data)
