"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

ReviewTemplateUpdateStatus: TypeAlias = Literal[
    "CURRENT",
    "LENS_NOT_CURRENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CURRENT",
        "LENS_NOT_CURRENT",
    )
)


def serialize_json(value: ReviewTemplateUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> ReviewTemplateUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReviewTemplateUpdateStatus value: {data!r}"
        )
    return cast(ReviewTemplateUpdateStatus, data)
