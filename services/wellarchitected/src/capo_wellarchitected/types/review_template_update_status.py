"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateUpdateStatus``."""

from typing import Literal, TypeAlias, cast

ReviewTemplateUpdateStatus: TypeAlias = Literal[
    "CURRENT",
    "LENS_NOT_CURRENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplateUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> ReviewTemplateUpdateStatus:
    return cast(ReviewTemplateUpdateStatus, data)
