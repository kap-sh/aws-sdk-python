"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a test case.</p>"""
TestCaseStatus: TypeAlias = Literal[
    "PUBLISHED",
    "SAVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseStatus) -> str:
    return value


def deserialize_json(data: str) -> TestCaseStatus:
    return cast(TestCaseStatus, data)
