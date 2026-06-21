"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetSortAttribute``."""

from typing import Literal, TypeAlias, cast

TestSetSortAttribute: TypeAlias = Literal[
    "TestSetName",
    "LastUpdatedDateTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSetSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> TestSetSortAttribute:
    return cast(TestSetSortAttribute, data)
