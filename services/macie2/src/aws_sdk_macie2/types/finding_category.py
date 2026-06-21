"""Generated from Smithy shape ``com.amazonaws.macie2#FindingCategory``."""

from typing import Literal, TypeAlias, cast

"""<p>The category of the finding. Possible values are:</p>"""
FindingCategory: TypeAlias = Literal[
    "CLASSIFICATION",
    "POLICY",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingCategory) -> str:
    return value


def deserialize_json(data: str) -> FindingCategory:
    return cast(FindingCategory, data)
