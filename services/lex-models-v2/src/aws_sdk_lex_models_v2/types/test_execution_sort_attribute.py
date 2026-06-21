"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionSortAttribute``."""

from typing import Literal, TypeAlias, cast

TestExecutionSortAttribute: TypeAlias = Literal[
    "TestSetName",
    "CreationDateTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> TestExecutionSortAttribute:
    return cast(TestExecutionSortAttribute, data)
