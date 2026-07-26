"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetStatus``."""

from typing import Literal, TypeAlias, cast

TestSetStatus: TypeAlias = Literal[
    "Importing",
    "PendingAnnotation",
    "Deleting",
    "ValidationError",
    "Ready",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSetStatus) -> str:
    return value


def deserialize_json(data: str) -> TestSetStatus:
    return cast(TestSetStatus, data)
