"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseEntryPointType``."""

from typing import Literal, TypeAlias, cast

TestCaseEntryPointType: TypeAlias = Literal[
    "VOICE_CALL",
    "CHAT",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseEntryPointType) -> str:
    return value


def deserialize_json(data: str) -> TestCaseEntryPointType:
    return cast(TestCaseEntryPointType, data)
