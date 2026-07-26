"""Generated from Smithy shape ``com.amazonaws.qapps#SubmissionMutationKind``."""

from typing import Literal, TypeAlias, cast

SubmissionMutationKind: TypeAlias = Literal[
    "edit",
    "delete",
    "add",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubmissionMutationKind) -> str:
    return value


def deserialize_json(data: str) -> SubmissionMutationKind:
    return cast(SubmissionMutationKind, data)
