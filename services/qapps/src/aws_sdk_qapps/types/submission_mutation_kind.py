"""Generated from Smithy shape ``com.amazonaws.qapps#SubmissionMutationKind``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

SubmissionMutationKind: TypeAlias = Literal[
    "edit",
    "delete",
    "add",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "edit",
        "delete",
        "add",
    )
)


def serialize_json(value: SubmissionMutationKind) -> str:
    return value


def deserialize_json(data: str) -> SubmissionMutationKind:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubmissionMutationKind value: {data!r}")
    return cast(SubmissionMutationKind, data)
