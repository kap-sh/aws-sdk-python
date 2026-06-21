"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestResultTypeFilter``."""

from typing import Literal, TypeAlias, cast

TestResultTypeFilter: TypeAlias = Literal[
    "OverallTestResults",
    "ConversationLevelTestResults",
    "IntentClassificationTestResults",
    "SlotResolutionTestResults",
    "UtteranceLevelResults",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestResultTypeFilter) -> str:
    return value


def deserialize_json(data: str) -> TestResultTypeFilter:
    return cast(TestResultTypeFilter, data)
