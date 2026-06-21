"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AssessmentInvoker``."""

from typing import Literal, TypeAlias, cast

AssessmentInvoker: TypeAlias = Literal[
    "User",
    "System",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentInvoker) -> str:
    return value


def deserialize_json(data: str) -> AssessmentInvoker:
    return cast(AssessmentInvoker, data)
