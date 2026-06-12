"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

"""<p>The status of a test case.</p>"""
TestCaseStatus: TypeAlias = Literal[
    "PUBLISHED",
    "SAVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISHED",
        "SAVED",
    )
)


def serialize_json(value: TestCaseStatus) -> str:
    return value


def deserialize_json(data: str) -> TestCaseStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestCaseStatus value: {data!r}")
    return cast(TestCaseStatus, data)
