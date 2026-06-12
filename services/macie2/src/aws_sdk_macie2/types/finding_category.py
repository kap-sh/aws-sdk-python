"""Generated from Smithy shape ``com.amazonaws.macie2#FindingCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The category of the finding. Possible values are:</p>"""
FindingCategory: TypeAlias = Literal[
    "CLASSIFICATION",
    "POLICY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLASSIFICATION",
        "POLICY",
    )
)


def serialize_json(value: FindingCategory) -> str:
    return value


def deserialize_json(data: str) -> FindingCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingCategory value: {data!r}")
    return cast(FindingCategory, data)
