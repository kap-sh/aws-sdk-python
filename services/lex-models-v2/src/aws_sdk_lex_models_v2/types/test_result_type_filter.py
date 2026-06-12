"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestResultTypeFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TestResultTypeFilter: TypeAlias = Literal[
    "OverallTestResults",
    "ConversationLevelTestResults",
    "IntentClassificationTestResults",
    "SlotResolutionTestResults",
    "UtteranceLevelResults",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OverallTestResults",
        "ConversationLevelTestResults",
        "IntentClassificationTestResults",
        "SlotResolutionTestResults",
        "UtteranceLevelResults",
    )
)


def serialize_json(value: TestResultTypeFilter) -> str:
    return value


def deserialize_json(data: str) -> TestResultTypeFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestResultTypeFilter value: {data!r}")
    return cast(TestResultTypeFilter, data)
